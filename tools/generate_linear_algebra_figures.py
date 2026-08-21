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
CANON_CH1 = PART / "figures"
CANON_CH2 = PART / "figures"
CANON_CH3 = PART / "figures"
PART2 = ROOT / "数学" / "線形代数" / "第II部 連立一次方程式と部分空間"
CANON_CH4 = PART2 / "figures"
CANON_CH5 = PART2 / "figures"
CANON_CH6 = PART2 / "figures"
PART3 = ROOT / "数学" / "線形代数" / "第III部 行列式――空間の伸び縮みを測る"
CANON_CH7 = PART3 / "figures"
CANON_CH8 = PART3 / "figures"

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


def polygon(ax, points, color=BLUE, alpha=0.2, label=None):
    points = np.asarray(points)
    closed = np.vstack([points, points[0]])
    ax.fill(closed[:, 0], closed[:, 1], color=color, alpha=alpha, label=label)
    ax.plot(closed[:, 0], closed[:, 1], color=color, linewidth=2)


def canonical_ch1():
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.2))
    setup_2d(axes[0], (-1, 5), (-1, 5), r"Vector $v=(3,2)$")
    arrow(axes[0], (0, 0), (3, 2), BLUE, r"$v$")
    axes[0].plot([3, 3], [0, 2], "--", color=GRAY); axes[0].plot([0, 3], [2, 2], "--", color=GRAY)
    setup_2d(axes[1], (-1, 5), (-1, 5), r"$3e_1+2e_2$")
    arrow(axes[1], (0, 0), (3, 0), ORANGE, r"$3e_1$")
    arrow(axes[1], (3, 0), (0, 2), GREEN, r"$2e_2$")
    arrow(axes[1], (0, 0), (3, 2), BLUE, r"$v$")
    setup_2d(axes[2], (-1, 8), (-1, 9), r"$Ax=2a_1+3a_2$")
    arrow(axes[2], (0, 0), (2, 4), BLUE, r"$2a_1$")
    arrow(axes[2], (2, 4), (3, 3), ORANGE, r"$3a_2$")
    arrow(axes[2], (0, 0), (5, 7), GREEN, r"$Ax$")
    save(fig, CANON_CH1 / "ch1-vectors-coordinates-matrix-product.svg")


def canonical_ch2():
    fig, axes = plt.subplots(2, 2, figsize=(9.4, 8.4))
    setup_2d(axes[0, 0], (-4, 4), (-3, 3), "One vector spans a line")
    t = np.linspace(-2, 2, 50); axes[0, 0].plot(2*t, t, color=BLUE, linewidth=3)
    arrow(axes[0, 0], (0, 0), (2, 1), BLUE, r"$v$")
    setup_2d(axes[0, 1], (-1, 3), (-1, 3), r"Dependent: $v_3=v_1+v_2$")
    arrow(axes[0, 1], (0, 0), (1, 0), BLUE, r"$v_1$"); arrow(axes[0, 1], (0, 0), (0, 1), ORANGE, r"$v_2$"); arrow(axes[0, 1], (0, 0), (1, 1), PURPLE, r"$v_3$")
    setup_2d(axes[1, 0], (-3, 3), (-3, 3), "Two different bases")
    arrow(axes[1, 0], (0, 0), (1, 0), BLUE, r"$e_1$"); arrow(axes[1, 0], (0, 0), (0, 1), ORANGE, r"$e_2$")
    arrow(axes[1, 0], (0, 0), (1, 1), GREEN, r"$b_1$"); arrow(axes[1, 0], (0, 0), (1, -1), PURPLE, r"$b_2$")
    setup_2d(axes[1, 1], (-1, 5), (-3, 3), r"Same $v$: coordinates $(3,1)$ and $(2,1)$")
    arrow(axes[1, 1], (0, 0), (3, 1), GREEN, r"$v$")
    arrow(axes[1, 1], (0, 0), (2, 2), BLUE, r"$2b_1$"); arrow(axes[1, 1], (2, 2), (1, -1), ORANGE, r"$+b_2$")
    save(fig, CANON_CH2 / "ch2-span-independence-basis-coordinates.svg")


def transform_grid(ax, matrix, title):
    setup_2d(ax, (-3.2, 3.2), (-3.2, 3.2), title)
    for c in np.linspace(-2, 2, 5):
        p = np.array([[-2, c], [2, c]]) @ matrix.T; ax.plot(p[:, 0], p[:, 1], color="#bfdbfe", linewidth=1)
        p = np.array([[c, -2], [c, 2]]) @ matrix.T; ax.plot(p[:, 0], p[:, 1], color="#fed7aa", linewidth=1)
    arrow(ax, (0, 0), matrix[:, 0], BLUE, r"$T(e_1)$", width=0.02)
    arrow(ax, (0, 0), matrix[:, 1], ORANGE, r"$T(e_2)$", width=0.02)


def canonical_ch3():
    mats = [(np.diag([2, 1]), "Horizontal stretch"), (np.diag([1, -1]), "Reflection"),
            (np.array([[0, -1], [1, 0]]), "90-degree rotation"), (np.array([[1, 1], [0, 1]]), "Shear")]
    fig, axes = plt.subplots(2, 2, figsize=(9, 9))
    for ax, (m, title) in zip(axes.flat, mats): transform_grid(ax, m, title)
    save(fig, CANON_CH3 / "ch3-four-linear-transformations.svg")

    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2))
    triangle = np.array([[0, 0], [1, 0], [0.5, 1]])
    matrices = [np.eye(2), np.diag([2, 1]), np.array([[0, -1], [1, 0]]) @ np.diag([2, 1])]
    titles = ["Input", "First: stretch", "Then: rotate"]
    for ax, m, title in zip(axes, matrices, titles):
        setup_2d(ax, (-2.5, 2.5), (-1, 2.8), title); polygon(ax, triangle @ m.T, GREEN)
    save(fig, CANON_CH3 / "ch3-composition-order.svg")

    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.4))
    setup_2d(axes[0], (-3, 3), (-3, 3), r"Kernel of $T(x,y)=(x,0)$")
    axes[0].plot([0, 0], [-3, 3], color=PURPLE, linewidth=4); axes[0].text(.15, 2.3, r"$\ker T$", color=PURPLE)
    setup_2d(axes[1], (-3, 3), (-3, 3), r"Image of $T(x,y)=(x,0)$")
    axes[1].plot([-3, 3], [0, 0], color=GREEN, linewidth=4); axes[1].text(1.7, .2, r"$\mathrm{Im}\,T$", color=GREEN)
    save(fig, CANON_CH3 / "ch3-kernel-and-image.svg")

    fig = plt.figure(figsize=(10, 4.6)); ax1 = fig.add_subplot(121, projection="3d"); ax2 = fig.add_subplot(122)
    for v, c, lab in [(np.array([1,0,0]), BLUE, r"$e_1$"), (np.array([0,1,0]), ORANGE, r"$e_2$"), (np.array([0,0,1]), PURPLE, r"$e_3$")]:
        ax1.quiver(0,0,0,*v,color=c,arrow_length_ratio=.15); ax1.text(*(v*1.1),lab,color=c)
    ax1.set(xlabel="x",ylabel="y",zlabel="z",title="Three input directions"); ax1.set_box_aspect((1,1,1))
    setup_2d(ax2, (-.5, 2), (-.5, 2), r"Their images in $\mathbb{R}^2$")
    for v,c,lab in [(np.array([1,0]),BLUE,r"$T(e_1)$"),(np.array([0,1]),ORANGE,r"$T(e_2)$"),(np.array([1,1]),PURPLE,r"$T(e_3)$")]: arrow(ax2,(0,0),v,c,lab,width=.015)
    save(fig, CANON_CH3 / "ch3-r3-to-r2.svg")


def canonical_ch4():
    fig = plt.figure(figsize=(12.5, 4.2))
    cases = [("Unique solution", [(1, 0, -1), (0, 1, -.5)]), ("Infinitely many", [(1, 0, -1), (2, 0, -2)]), ("No solution", [(1, 0, -1), (1, 0, 1)])]
    x = np.linspace(-3,3,100)
    for i,(title, lines) in enumerate(cases,1):
        ax=fig.add_subplot(1,3,i); setup_2d(ax,(-3,3),(-3,3),title)
        for a,b,c in lines:
            if b == 0: ax.axvline(-c/a,linewidth=2.5)
            else: ax.plot(x,(-a*x-c)/b,linewidth=2.5)
    save(fig, CANON_CH4 / "ch4-three-solution-cases.svg")

    fig=plt.figure(figsize=(7,5.4)); ax=fig.add_subplot(111,projection="3d")
    xx,yy=np.meshgrid(np.linspace(-2,2,15),np.linspace(-2,2,15)); zz=xx+2*yy-3
    ax.plot_surface(xx,yy,zz,alpha=.35,color=BLUE,edgecolor="#bfdbfe"); ax.set(xlabel="x",ylabel="y",zlabel="z",title=r"$x+2y-z=3$"); ax.set_box_aspect((1,1,1))
    save(fig,CANON_CH4/"ch4-one-equation-is-a-plane.svg")

    fig,ax=plt.subplots(figsize=(6.5,5)); setup_2d(ax,(-4,4),(-3,3),r"$x=x_p+t v$: translated null space")
    t=np.linspace(-3,3,100); ax.plot(t+1,t*.5+1,color=GREEN,linewidth=4); ax.scatter([1],[1],color=ORANGE,s=60); ax.text(1.15,1.1,r"$x_p$",color=ORANGE)
    arrow(ax,(1,1),(2,1),GREEN,r"$v\in\mathrm{Null}(A)$",width=.02); save(fig,CANON_CH4/"ch4-general-solution-affine-line.svg")


def canonical_ch5():
    fig=plt.figure(figsize=(10.5,4.6)); ax1=fig.add_subplot(121,projection="3d"); ax2=fig.add_subplot(122)
    xx,yy=np.meshgrid(np.linspace(-2,2,10),np.linspace(-2,2,10)); ax1.plot_surface(xx,yy,np.zeros_like(xx),alpha=.3,color=GREEN); ax1.quiver(0,0,0,0,0,2,color=PURPLE); ax1.set(title="Projection: 2 directions remain, 1 is lost",xlabel="x",ylabel="y",zlabel="z")
    setup_2d(ax2,(-3,3),(-3,3),"Column space: reachable outputs"); ax2.axhspan(-3,3,color=GREEN,alpha=.12); arrow(ax2,(0,0),(1,0),BLUE,r"$a_1$"); arrow(ax2,(0,0),(0,1),ORANGE,r"$a_2$")
    save(fig,CANON_CH5/"ch5-column-space-rank-nullity.svg")
    fig=plt.figure(figsize=(7,5.4)); ax=fig.add_subplot(111,projection="3d"); t=np.linspace(-3,3,50); ax.plot(t,t,-t,color=PURPLE,linewidth=4); ax.quiver(0,0,0,1,1,-1,color=PURPLE); ax.set(title=r"Null space: $t(1,1,-1)$",xlabel="x",ylabel="y",zlabel="z"); save(fig,CANON_CH5/"ch5-null-space-line.svg")


def canonical_ch6():
    fig,axes=plt.subplots(1,2,figsize=(9.4,4.4))
    transform_grid(axes[0],np.array([[2,1],[1,1]]),"Invertible: two directions remain")
    transform_grid(axes[1],np.array([[1,2],[2,4]]),"Not invertible: plane collapses")
    save(fig,CANON_CH6/"ch6-invertible-vs-singular.svg")
    fig,axes=plt.subplots(1,3,figsize=(12.5,4)); tri=np.array([[0,0],[1,0],[.3,1]])
    mats=[np.eye(2),np.array([[2,1],[0,1]]),np.eye(2)]; titles=["Input",r"Apply $A$",r"Apply $A^{-1}$"]
    for ax,m,title in zip(axes,mats,titles): setup_2d(ax,(-.5,3),(-.5,2),title); polygon(ax,tri@m.T,GREEN)
    save(fig,CANON_CH6/"ch6-inverse-restores-input.svg")


def canonical_ch7():
    fig,axes=plt.subplots(1,3,figsize=(13,4.2)); examples=[(np.array([[2,0],[0,1]]),"Positive area"),(np.array([[0,1],[1,0]]),"Orientation reversed"),(np.array([[1,2],[2,4]]),"Area zero")]
    square=np.array([[0,0],[1,0],[1,1],[0,1]])
    for ax,(m,title) in zip(axes,examples): setup_2d(ax,(-1,3),(-1,3),title); polygon(ax,square@m.T,BLUE)
    save(fig,CANON_CH7/"ch7-oriented-area-and-zero.svg")
    fig=plt.figure(figsize=(7,5.5)); ax=fig.add_subplot(111,projection="3d");
    verts=np.array([[0,0,0],[2,0,0],[0,1,0],[0,0,1.5]]); origin=verts[0]
    for v,c,lab in zip(verts[1:],[BLUE,ORANGE,GREEN],[r"$a_1$",r"$a_2$",r"$a_3$"]): ax.quiver(*origin,*(v-origin),color=c,arrow_length_ratio=.12); ax.text(*v,lab,color=c)
    ax.set(title="Three columns determine volume",xlabel="x",ylabel="y",zlabel="z"); save(fig,CANON_CH7/"ch7-three-columns-volume.svg")


def canonical_ch8():
    fig,axes=plt.subplots(1,3,figsize=(13,4.2)); base=np.array([[0,0],[1,0],[1,1],[0,1]]); mats=[np.eye(2),np.array([[1,1],[0,1]]),np.array([[2,2],[0,1]])]; titles=["Original area", "Add one row: unchanged", "Scale one row: doubled"]
    for ax,m,title in zip(axes,mats,titles): setup_2d(ax,(-.5,4),(-.5,2),title); polygon(ax,base@m.T,BLUE)
    save(fig,CANON_CH8/"ch8-row-operations-and-area.svg")
    fig,axes=plt.subplots(1,3,figsize=(13,4.2)); tri=np.array([[0,0],[1,0],[.2,1]]); mats=[np.eye(2),np.diag([2,1]),np.array([[1,1],[0,1]])@np.diag([2,1])]; titles=["Input",r"$B$: area $\times2$",r"$A B$: area $\times2\times1$"]
    for ax,m,title in zip(axes,mats,titles): setup_2d(ax,(-.5,3),(-.5,2),title); polygon(ax,tri@m.T,GREEN)
    save(fig,CANON_CH8/"ch8-determinant-of-composition.svg")
    fig,ax=plt.subplots(figsize=(6.6,5.2)); setup_2d(ax,(-1,5),(-1,5),"Cramer's rule as an area ratio"); a1=np.array([3,1]); a2=np.array([1,3]); b=2*a1+a2
    polygon(ax,[[0,0],a1,a1+a2,a2],BLUE,.15,r"$\det(a_1,a_2)$"); polygon(ax,[[0,0],b,b+a2,a2],ORANGE,.15,r"$\det(b,a_2)$"); arrow(ax,(0,0),a1,BLUE,r"$a_1$"); arrow(ax,(0,0),a2,GREEN,r"$a_2$"); arrow(ax,(0,0),b,ORANGE,r"$b$"); ax.legend(fontsize=9); save(fig,CANON_CH8/"ch8-cramers-rule-area-ratio.svg")


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
    canonical_ch1()
    canonical_ch2()
    canonical_ch3()
    canonical_ch4()
    canonical_ch5()
    canonical_ch6()
    canonical_ch7()
    canonical_ch8()
    print("Generated legacy and canonical chapter figures.")
