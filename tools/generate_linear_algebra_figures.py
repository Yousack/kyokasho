import os
from pathlib import Path

MPL_CACHE = Path(__file__).resolve().parent / ".matplotlib"
MPL_CACHE.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CACHE))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PART = ROOT / "数学" / "線形代数" / "第I部 ベクトルと線形変換"
CH1 = PART / "第1章 ベクトル――向きと大きさをもつ量" / "figures"
CH2 = PART / "第2章 線形変換――形を保つ写像" / "figures"

BLUE = "#2563eb"
ORANGE = "#ea580c"
GREEN = "#16a34a"
PURPLE = "#7c3aed"
GRAY = "#64748b"


def setup_2d(ax, xlim, ylim, title):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axhline(0, color="#94a3b8", linewidth=0.9)
    ax.axvline(0, color="#94a3b8", linewidth=0.9)
    ax.grid(True, color="#e2e8f0", linewidth=0.8)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(title, fontsize=12)
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def arrow(ax, start, delta, color, label, width=0.035):
    ax.arrow(*start, *delta, length_includes_head=True, head_width=0.18,
             head_length=0.25, linewidth=2.2, color=color, width=width)
    end = np.asarray(start) + np.asarray(delta)
    ax.text(end[0] + 0.12, end[1] + 0.12, label, color=color, fontsize=10)


def save(fig, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plane_vector():
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    setup_2d(ax, (0, 5), (0, 5), r"$\overrightarrow{AB}=(4-1,\,4-2)=(3,2)$")
    ax.plot([1, 4], [2, 2], "--", color=GRAY)
    ax.plot([4, 4], [2, 4], "--", color=GRAY)
    arrow(ax, (1, 2), (3, 2), BLUE, r"$B=(4,4)$")
    ax.scatter([1], [2], color=ORANGE, s=45, zorder=3)
    ax.text(0.55, 1.72, r"$A=(1,2)$", color=ORANGE)
    ax.text(2.25, 1.68, r"$\Delta x=3$", color=GRAY)
    ax.text(4.08, 2.85, r"$\Delta y=2$", color=GRAY)
    save(fig, CH1 / "1-1-1-example-1-plane-vector.png")


def space_vector():
    fig = plt.figure(figsize=(6.8, 5.4))
    ax = fig.add_subplot(111, projection="3d")
    a = np.array([1, -2, 3])
    d = np.array([3, 2, -4])
    b = a + d
    ax.quiver(*a, *d, color=BLUE, linewidth=2.5, arrow_length_ratio=0.12)
    ax.scatter(*a, color=ORANGE, s=45)
    ax.scatter(*b, color=GREEN, s=45)
    ax.text(*(a + [0.1, 0.1, 0.1]), "A (1, -2, 3)", color=ORANGE)
    ax.text(*(b + [0.1, 0.1, 0.1]), "B (4, 0, -1)", color=GREEN)
    ax.set(xlabel="x", ylabel="y", zlabel="z", title=r"$\overrightarrow{AB}=(3,2,-4)$")
    ax.set_box_aspect((1, 1, 1))
    save(fig, CH1 / "1-1-1-example-2-space-vector.png")


def independent_vectors():
    fig, ax = plt.subplots(figsize=(6.2, 5.2))
    setup_2d(ax, (-0.5, 2.7), (-0.5, 2.7), "Two non-parallel directions")
    arrow(ax, (0, 0), (1, 2), BLUE, r"$v_1=(1,2)$")
    arrow(ax, (0, 0), (2, 1), ORANGE, r"$v_2=(2,1)$")
    ax.text(0.78, 0.63, "not parallel", color=GRAY, rotation=-20)
    save(fig, CH1 / "1-1-4-independent-vectors.png")


def basis_images():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.4))
    setup_2d(axes[0], (-1.5, 2.7), (-0.5, 3.6), "Images of basis vectors")
    arrow(axes[0], (0, 0), (2, 1), BLUE, r"$T(e_1)$")
    arrow(axes[0], (0, 0), (-1, 3), ORANGE, r"$T(e_2)$")
    setup_2d(axes[1], (-0.8, 7.2), (-0.8, 10.8), "Weighted sum")
    arrow(axes[1], (0, 0), (8, 4), BLUE, r"$4T(e_1)$", width=0.06)
    arrow(axes[1], (8, 4), (-2, 6), ORANGE, r"$+2T(e_2)$", width=0.06)
    arrow(axes[1], (0, 0), (6, 10), GREEN, r"$(6,10)$", width=0.04)
    save(fig, CH2 / "1-2-1-basis-images.png")


def linear_map():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.5))
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    matrix = np.array([[2, -1], [0, 3]])
    mapped = square @ matrix.T
    setup_2d(axes[0], (-0.4, 1.4), (-0.4, 1.4), "Before")
    axes[0].fill(square[:, 0], square[:, 1], color=BLUE, alpha=0.25)
    axes[0].plot(square[:, 0], square[:, 1], color=BLUE, linewidth=2)
    setup_2d(axes[1], (-1.4, 2.4), (-0.4, 3.4), r"After $T(x,y)=(2x-y,3y)$")
    axes[1].fill(mapped[:, 0], mapped[:, 1], color=GREEN, alpha=0.25)
    axes[1].plot(mapped[:, 0], mapped[:, 1], color=GREEN, linewidth=2)
    save(fig, CH2 / "1-2-3-linear-map.png")


def nonlinear_maps():
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.4))
    setup_2d(axes[0], (-0.5, 2.0), (-0.5, 1.5), r"Translation: $F(0)\ne0$")
    arrow(axes[0], (0, 0), (1, 0), ORANGE, r"$F(0)=(1,0)$")
    axes[0].scatter([0], [0], color=GRAY, s=35)
    setup_2d(axes[1], (-0.5, 4.8), (-0.5, 2.8), "Scaling is not preserved")
    axes[1].scatter([1, 2, 2, 4], [1, 2, 2, 2], color=[BLUE, BLUE, ORANGE, ORANGE], s=45)
    axes[1].plot([1, 2], [1, 2], color=BLUE, label=r"$G(v),\ 2G(v)$")
    axes[1].plot([2, 4], [2, 2], color=ORANGE, label=r"$2G(v),\ G(2v)$")
    axes[1].legend(loc="upper left", fontsize=9)
    save(fig, CH2 / "1-2-3-nonlinear-maps.png")


def kernel_and_image():
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.6))
    t = np.linspace(-3, 3, 100)
    setup_2d(axes[0], (-3.3, 3.3), (-3.3, 3.3), "Input plane and kernel")
    axes[0].plot(t, -t, color=PURPLE, linewidth=3, label=r"$\ker T: y=-x$")
    axes[0].legend()
    setup_2d(axes[1], (-2.3, 2.3), (-4.6, 4.6), "All outputs lie on one line")
    axes[1].plot(t / 1.5, 2 * t / 1.5, color=GREEN, linewidth=3,
                 label=r"$\mathrm{Im}\,T=\mathrm{span}\{(1,2)\}$")
    arrow(axes[1], (0, 0), (1, 2), GREEN, r"$(1,2)$", width=0.025)
    axes[1].legend(loc="upper left", fontsize=9)
    save(fig, CH2 / "1-2-6-kernel-and-image.png")


if __name__ == "__main__":
    plane_vector()
    space_vector()
    independent_vectors()
    basis_images()
    linear_map()
    nonlinear_maps()
    kernel_and_image()
    print("Generated 7 figures.")
