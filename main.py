import argparse
from src.animation import generate_animation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser for animation generator")

    parser.add_argument(
        "-f",
        action="store",
        dest="f",
        help="Function to optimize. Has to be defined in "
        'src/functions.py. Currently availables: "beale", '
        '"rosenbrock", "rastrigin", "levi_13" and "beale"',
        default="beale",
    )

    parser.add_argument(
        "-p",
        action="store",
        dest="n_particles",
        help="Number of particles",
        type=int,
        default=100,
    )

    parser.add_argument(
        "-w",
        action="store",
        dest="w",
        help="Inertia coefficient",
        type=float,
        default=1,
    )

    parser.add_argument(
        "-c1",
        action="store",
        dest="c1",
        help="Cognitive coefficient",
        type=float,
        default=0.5,
    )

    parser.add_argument(
        "-c2",
        action="store",
        dest="c2",
        help="Social coefficient",
        type=float,
        default=1.0,
    )

    parser.add_argument(
        "-s",
        action="store",
        dest="n_steps",
        help="Number of optimization steps",
        type=int,
        default=200,
    )

    parser.add_argument(
        "-r",
        action="store",
        dest="range",
        default=[-5, 5],
        type=int,
        nargs="*",
        help="Range of plot and initialization",
    )

    parser.add_argument(
        "-v",
        action="store",
        dest="fps",
        default=10,
        type=int,
        help="Frames per second in the output animation",
    )

    parser.add_argument(
        "-o",
        action="store",
        dest="filepath",
        default="animation.gif",
        type=str,
        help="Output gif file path",
    )

    parser.add_argument(
        "-rd",
        action="store",
        dest="seed",
        default=655321,
        type=int,
        help="Random seed",
    )

    results = parser.parse_args()

    generate_animation(
        f=results.f,
        n_particles=results.n_particles,
        n_steps=results.n_steps,
        w=results.w,
        c1=results.c1,
        c2=results.c2,
        init_range=results.range,
        plot_range=results.range,
        fps=results.fps,
        filepath=results.filepath,
        seed=results.seed,
    )
