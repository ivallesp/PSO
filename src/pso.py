import numpy as np


class PSO:
    def __init__(self, n_particles, n_dims, w, c1, c2, init_range):
        """Particle swarm optimization algorithm

        Args:
            n_particles (int): Number of particles to use
            n_dims (int): Number of dimensions of the objective function
            w (float): Inertia coefficient
            c1 (float): Cognitive coefficient
            c2 (float): Social coefficient
            init_range (list): Initialization range for the rand uniform function
        """
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.init_range = init_range
        self.pos, self.delta_pos = self._initialize(n_particles, n_dims, init_range)
        # Best particle positions and values
        self.best_p_pos = self.pos.copy()
        self.best_p_val = np.ones(n_particles) * np.Inf

    @property
    def best_g_val(self):
        best = np.min(self.best_p_val)
        return best

    @property
    def best_g_pos(self):
        idx = np.argmin(self.best_p_val)
        return self.best_p_pos[[idx]]

    @staticmethod
    def _initialize(n_particles, n_dims, init_range):
        _max, _min = max(init_range), min(init_range)
        pos = np.random.uniform(low=_min, high=_max, size=(n_particles, n_dims))
        delta_pos = np.zeros((n_particles, n_dims))
        return pos, delta_pos

    def step(self, evaluations):
        # Update the best particle values and positions
        improvements = evaluations < self.best_p_val
        self.best_p_val[improvements] = evaluations[improvements]
        self.best_p_pos[improvements] = self.pos[improvements]

        # Calculate the inertia component
        r = np.random.uniform(low=0, high=self.w, size=(self.pos.shape[0], 1))
        inertia = self.delta_pos * r

        # Calculate the cognitive component
        r = np.random.uniform(low=0, high=self.c1, size=(self.pos.shape[0], 1))
        cognitive = (self.best_p_pos - self.pos) * r

        # Calculate the social component
        r = np.random.uniform(low=0, high=self.c2, size=(self.pos.shape[0], 1))
        social = (self.best_g_pos - self.pos) * r

        self.delta_pos = inertia + cognitive + social
        self.pos = self.pos + self.delta_pos
        return self.pos
