import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QPen, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QPushButton, QMainWindow
)
from scipy.ndimage import zoom


class HeatmapWidget(QWidget):
    def __init__(self, Z, parent=None):
        super().__init__(parent)
        self.Z = Z
        self.h, self.w = Z.shape

        # Initialize optional UI bindings
        self.counter_display = None
        self.max_display = None
        self.strategy_display = None

        # Animation state
        self.i = 0
        self.j = 0
        self.step_count = 0
        self.max_val = float("-inf")
        self.rect_color = Qt.green
        self.velocity = np.array([0, 0], dtype=float)
        self.strategy = self.raster_step
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_step)

        # Create the heatmap image
        norm = plt.Normalize(vmin=Z.min(), vmax=Z.max())
        rgb = plt.cm.jet_r(norm(Z))[:, :, :3]
        rgb = (rgb * 255).astype(np.uint8)
        rgb = np.ascontiguousarray(rgb)
        qimg = QImage(rgb.data, self.w, self.h, 3 * self.w, QImage.Format_RGB888).copy()
        self.pixmap = QPixmap.fromImage(qimg)

        self.reset_state()

    # --------------------- RESET ---------------------
    def reset_state(self):
        """Reset all animation variables"""
        if self.strategy == self.raster_step:
            self.i, self.j = 0, 0
        else:
            self.i = np.random.randint(self.h)
            self.j = np.random.randint(self.w)

        self.step_count = 0
        self.max_val = float("-inf")
        self.rect_color = Qt.green
        self.velocity = np.array([0, 0], dtype=float)

        if self.counter_display:
            self.counter_display.setText("0")
        if self.max_display:
            self.max_display.setText("")
        self.update()

    # --------------------- HEURISTICS ---------------------
    def raster_step(self, i, j, Z):
        j += 1
        if j >= self.w:
            j = 0
            i += 1
        if i >= self.h:
            i = 0
        return i, j

    def gradient_ascent_step(self, i, j, Z):
        h, w = Z.shape
        best = (Z[i, j], i, j)
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and (di or dj):
                    if Z[ni, nj] > best[0]:
                        best = (Z[ni, nj], ni, nj)
        return best[1], best[2]

    def newton_step(self, i, j, Z):
        h, w = Z.shape
        def safe(a, b): return np.clip(a, 0, h - 1), np.clip(b, 0, w - 1)
        dZdi = (Z[safe(i+1, j)[0], j] - Z[safe(i-1, j)[0], j]) / 2
        dZdj = (Z[i, safe(i, j+1)[1]] - Z[i, safe(i, j-1)[1]]) / 2
        d2Zdi2 = Z[safe(i+1, j)[0], j] - 2 * Z[i, j] + Z[safe(i-1, j)[0], j]
        d2Zdj2 = Z[i, safe(i, j+1)[1]] - 2 * Z[i, j] + Z[i, safe(i, j-1)[1]]
        step_i = int(round(i + dZdi / (abs(d2Zdi2) + 1e-5)))
        step_j = int(round(j + dZdj / (abs(d2Zdj2) + 1e-5)))
        return np.clip(step_i, 0, h - 1), np.clip(step_j, 0, w - 1)

    def pso_step(self, i, j, Z):
        grad = np.array([
            Z[min(i+1, self.h-1), j] - Z[max(i-1, 0), j],
            Z[i, min(j+1, self.w-1)] - Z[i, max(j-1, 0)]
        ])
        grad /= (np.linalg.norm(grad) + 1e-5)
        self.velocity = 0.7 * self.velocity + 0.3 * grad
        new = np.array([i, j]) + np.sign(self.velocity)
        new = np.clip(new, [0, 0], [self.h-1, self.w-1])
        return int(new[0]), int(new[1])

    def basin_step(self, i, j, Z):
        ni = np.clip(i + np.random.randint(-2, 3), 0, self.h-1)
        nj = np.clip(j + np.random.randint(-2, 3), 0, self.w-1)
        if Z[ni, nj] > Z[i, j]:
            return ni, nj
        else:
            return i, j

    def tree_step(self, i, j, Z):
        val = Z[i, j]
        if val < np.mean(Z):
            return max(i-1, 0), min(j+1, self.w-1)
        elif val < np.percentile(Z, 75):
            return min(i+1, self.h-1), j
        else:
            return i, min(j+1, self.w-1)

    # --------------------- ANIMATION ---------------------
    def next_step(self):
        val = self.Z[self.i, self.j]
        self.step_count += 1

        if self.counter_display:
            self.counter_display.setText(str(self.step_count))

        if val > self.max_val:
            self.max_val = val
            if self.max_display:
                self.max_display.setText(f"{self.max_val:.3f}")
            self.rect_color = Qt.red
            self.update()
            self.timer.stop()
            QTimer.singleShot(200, self.resume_after_pause)
            return

        self.i, self.j = self.strategy(self.i, self.j, self.Z)
        self.rect_color = Qt.green
        self.update()

    def resume_after_pause(self):
        self.i, self.j = self.strategy(self.i, self.j, self.Z)
        self.rect_color = Qt.green
        self.update()
        self.timer.start(40)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)
        painter.setPen(QPen(self.rect_color, 2))
        rect_w = self.width() / self.w
        rect_h = self.height() / self.h
        painter.drawRect(self.j * rect_w, self.i * rect_h, rect_w, rect_h)


class MainWindow(QMainWindow):
    def __init__(self, Z):
        super().__init__()
        self.setWindowTitle("Optimization Visualizer")

        widget = QWidget()
        layout = QVBoxLayout(widget)
        self.heatmap = HeatmapWidget(Z)
        layout.addWidget(self.heatmap)

        # Info + controls
        controls = QHBoxLayout()
        controls.addWidget(QLabel("Steps:"))
        steps_edit = QLineEdit(); steps_edit.setReadOnly(True)
        controls.addWidget(steps_edit)
        controls.addWidget(QLabel("Max:"))
        max_edit = QLineEdit(); max_edit.setReadOnly(True)
        controls.addWidget(max_edit)
        controls.addWidget(QLabel("Heuristic:"))
        combo = QComboBox()
        combo.addItems(["Raster", "Gradient Ascent", "Newton", "PSO", "Basin Hop"])
        controls.addWidget(combo)

        # Buttons
        self.start_btn = QPushButton("Start")
        self.reset_btn = QPushButton("Reset")
        controls.addWidget(self.start_btn)
        controls.addWidget(self.reset_btn)
        layout.addLayout(controls)

        self.setCentralWidget(widget)

        # Hook up displays
        self.heatmap.counter_display = steps_edit
        self.heatmap.max_display = max_edit

        # Hook up signals
        combo.currentTextChanged.connect(self.set_strategy)
        self.start_btn.clicked.connect(self.toggle_animation)
        self.reset_btn.clicked.connect(self.reset_animation)

    # --------------------- Button Actions ---------------------
    def set_strategy(self, name):
        strategies = {
            "Raster": self.heatmap.raster_step,
            "Gradient Ascent": self.heatmap.gradient_ascent_step,
            "Newton": self.heatmap.newton_step,
            "PSO": self.heatmap.pso_step,
            "Basin Hop": self.heatmap.basin_step,
            # "Decision Tree": self.heatmap.tree_step
        }
        self.heatmap.strategy = strategies.get(name, self.heatmap.raster_step)
        self.reset_animation()

    def toggle_animation(self):
        if self.heatmap.timer.isActive():
            self.heatmap.timer.stop()
            self.start_btn.setText("Start")
        else:
            self.heatmap.timer.start(40)
            self.start_btn.setText("Pause")

    def reset_animation(self):
        self.heatmap.timer.stop()
        self.start_btn.setText("Start")
        self.heatmap.reset_state()

# --------------------- Main ---------------------
def main():
    app = QApplication(sys.argv)
    Z = np.loadtxt("Z_clip.csv", delimiter=",")
    Z_small = zoom(Z, (40 / Z.shape[0], 40 / Z.shape[1]), order=3)
    w = MainWindow(Z_small)
    w.resize(700, 700)
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
