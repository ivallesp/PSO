import numpy as np
from src.pso import PSO
from src.functions import get_test_function
from celluloid import Camera

import matplotlib.pyplot as plt


def generate_animation(
    f,
    n_particles=100,
    n_steps=200,
    w=1.0,
    c1=0.5,
    c2=1.0,
    init_range=[-1, 1],
    plot_range=[-1, 1],
    fps=10,
    seed=655321,
    filepath="animation.gif",
):
    """Runs a PSO metaheuristic over the function provided and generates an
    animated gif.

    Args:
        f (name): Name of the function defined in functions.py to optimize.
        n_particles (int, optional): Number of particles. Defaults to 100.
        n_steps (int, optional): Number of opt. steps. Defaults to 200.
        w (float, optional): Inertia parameter. Defaults to 1.0.
        c1 (float, optional): Cognitive parameter. Defaults to 0.5.
        c2 (float, optional): Social parameter. Defaults to 1.0.
        init_range (list, optional): Range to random uniform the particles.
        Defaults to [-1, 1].
        plot_range (list, optional): X and Y limits. Defaults to [-1, 1].
        fps (int, optional): Frames per second of the animation. Defaults to
        10.
        filepath (str, optional): Filepath to save the animation. Defaults to
        "animation.gif".
    """
    np.random.seed(seed)
    # Retrieve the function specified
    f = get_test_function(f)
    # Generate the meshgrid and values for contour plot
    x = np.linspace(plot_range[0], plot_range[1], 50)
    y = np.linspace(plot_range[0], plot_range[1], 50)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Initialize the figure
    fig = plt.figure(figsize=(10, 8))
    camera = Camera(fig)

    # Initialize the algorithm
    pso = PSO(
        n_particles=n_particles, n_dims=2, w=w, c1=c1, c2=c2, init_range=init_range
    )

    for i in range(n_steps):
        # Plot positions
        ax = plt.axes(xlim=plot_range, ylim=plot_range)
        ax.contour(X, Y, np.log(Z))
        ax.scatter(pso.pos[:, 0], pso.pos[:, 1], c="b", s=4)
        camera.snap()
        # Evaluate positions
        evals = f(pso.pos[:, 0], pso.pos[:, 1])
        # Update positions
        pso.step(evaluations=evals)
    # Generate Animation
    animation = camera.animate()
    animation.save(filepath, writer="imagemagick", fps=10)
