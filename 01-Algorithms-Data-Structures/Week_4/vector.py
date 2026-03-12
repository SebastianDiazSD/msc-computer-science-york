from math import isclose
class Vector:
    def __init__(self, data):
        if not all(isinstance(v, (float, int)) for v in data):
            raise ValueError("All elements must be floats or ints.")

        # Copy of the input list to avoid external mutation
        self._vector = data.copy()

    def __repr__(self):
        return f"Vector({self._vector})"

    def __str__(self):
        """
        Returns a user-friendly string representation of the vector.
        Example: '<2.0, 4.0, 1.1>'
        """
        return f"<{', '.join(str(v) for v in self._vector)}>"

    def dim(self):
        """
        Returns the dimension of a vector (i.e. the number of values in a vector).
        """
        return len(self._vector)

    def get(self, index):
        """
        Returns the value at the given index.
        """
        if not (0 <= index < self.dim()):
            raise IndexError("Index out of range.")
        return self._vector[index]

    def set(self, index, value):
        """
        Sets the value at the given index to the new float value.
        """
        if not (0 <= index < self.dim()):
            raise IndexError("Index out of range.")
        if not isinstance(value, (float, int)):
            raise ValueError("Value must be a float or int.")
        self._vector[index] = value

    def scalar_product(self, scalar):
        """
        Returns a new Vector where each value is multiplied by the given scalar.
        The original vector is not modified.
        """
        if not isinstance(scalar, (float, int)):
            raise ValueError("Scalar must be a float or int.")
        new_values = [x * scalar for x in self._vector]
        return Vector(new_values)

    def add(self, other_vector):
        """
        Emulate the vector addition operator.

        Conditions:
        other_vector is a Vector instance and return None if it is not the case.
        both vectors have the same dimension, return None if it is not the case.

        """
        if not isinstance(other_vector, Vector):
            return None

        if self.dim() != other_vector.dim():
            return None

        list_sum=[]
        for i in range(self.dim()):
            added_values=self._vector[i]+other_vector._vector[i]
            list_sum.append(added_values)

        return list_sum

    def equals(self, other_vector):
        """
        Returns True if this vector is equal to another (same dimensions and values).
        Uses math.isclose() for float comparison.
        """
        if not isinstance(other_vector, Vector):
            return False
        if self.dim() != other_vector.dim():
            return False

        return all(isclose(self._vector[i], other_vector._vector[i]) for i in range(self.dim()))

    def __eq__(self, other_vector):
        return self.equals(other_vector)

    def __ne__(self, other_vector):
        return not self.__eq__(other_vector)

    def __add__(self, other_vector):
        return self.add(other_vector)

    def __mul__(self, scalar):
        return self.scalar_product(scalar)

    def __rmul__(self, scalar):
        return self.scalar_product(scalar)

    def __iadd__(self, other_vector):
        """
        In-place addition. Modifies current vector.
        """
        if not isinstance(other_vector, Vector) or self.dim() != other_vector.dim():
            raise ValueError("Incompatible vector for addition.")
        for i in range(self.dim()):
            self._vector[i] += other_vector._vector[i]
        return self

    def __imul__(self, scalar):
        """
        In-place scalar multiplication. Modifies current vector.
        """
        if not isinstance(scalar, (float, int)):
            raise ValueError("Scalar must be a number.")
        for i in range(self.dim()):
            self._vector[i] *= scalar
        return self


v1 = Vector([1.0, 2.0, 3.0])
v2 = Vector([0.0, 1.0, 3.0])

# Equality and inequality
print(v1 == v2)  # False
print(v1 != v2)  # True

# Operator +
v3 = v1 + v2
print(v3)  # <1.0, 3.0, 6.0>

# Operator *
v4 = v1 * 2
v5 = 2 * v1
print(v4)  # <2.0, 4.0, 6.0>
print(v5)  # <2.0, 4.0, 6.0>

# Operator +=
v1 += v2
print(v1)  # <1.0, 3.0, 6.0>

# Operator *=
v1 *= 2
print(v1)  # <2.0, 6.0, 12.0>
