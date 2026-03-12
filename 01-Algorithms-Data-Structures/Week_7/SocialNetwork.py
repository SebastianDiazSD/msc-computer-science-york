from user import User

sebas = User(1, "Sebaswrtgthr")
# sebas._id=5

print(sebas.get_name())


class SocialNetwork:

    def __init__(self, name):
        """Construct an instance of SocialNetwork.

        Args:
            name (str): the name of the network
        """
        self._name = name
        self._users = {}

    def create_user(self, id, name):
        if id not in self._users:
            new_user=User(id,name)
            self._users[id] = new_user
            return new_user
        else:
            raise ValueError("The user is already registered in the network")

    def get_user(self,id):
        if id in self._users:
            return self._users[id]
        else:
            raise ValueError("The user do not exist in the network")

    def add_relationship(self, user_one_id, user_two_id):
        # Check that both users exist
        if user_one_id not in self._users or user_two_id not in self._users:
            raise ValueError("One or both users do not exist.")

        user_one = self._users[user_one_id]
        user_two = self._users[user_two_id]

        # Add each user to the other's connections
        added1 = user_one.add_connection(user_two_id)
        added2 = user_two.add_connection(user_one_id)

        return added1 and added2  # Return True if both were added successfully

    def connexion_degree(self, source_id, target_id):
        # Return -1 if either user does not exist
        if source_id not in self._users or target_id not in self._users:
            return -1

        # Return -1 if source and target are the same
        if source_id == target_id:
            return 0  # Optional: could be considered 0 or -1

        # Use Breadth-First Search (BFS) up to 3 levels
        visited = []  # Keep track of visited users
        queue = [(source_id, 0)]  # Each item is (user_id, depth)

        while len(queue) > 0:
            current_id, depth = queue.pop(0)

            if depth >= 3:
                continue  # We only care about up to 3rd-degree

            current_user = self._users[current_id]
            connections = current_user.get_connections()

            for friend_id in connections:
                if friend_id == target_id:
                    return depth + 1  # Found the target!

                if friend_id not in visited:
                    visited.append(friend_id)
                    queue.append((friend_id, depth + 1))

        return -1  # Target not found within 3 degrees

    def get_close_network(self, user_id):
        # If user doesn't exist, return empty set
        if user_id not in self._users:
            return set()

        visited = []
        close_users = set()
        queue = [(user_id, 0)]

        while len(queue) > 0:
            current_id, depth = queue.pop(0)

            if depth >= 3:
                continue

            current_user = self._users[current_id]
            connections = current_user.get_connections()

            for friend_id in connections:
                if friend_id not in visited and friend_id != user_id:
                    visited.append(friend_id)
                    close_users.add(friend_id)
                    queue.append((friend_id, depth + 1))

        return close_users

    def closeness(self, user_id):
        # Step 1: Check if the user exists
        if user_id not in self._users:
            raise ValueError("User not found in the network.")

        # Step 2: Initialize
        total_users = len(self._users)
        visited = []
        distance_sum = 0
        queue = [(user_id, 0)]  # (current_user_id, current_distance)

        # Step 3: BFS to calculate distances
        while len(queue) > 0:
            current_id, dist = queue.pop(0)

            if current_id in visited:
                continue

            visited.append(current_id)

            # Don't count the distance to itself (0)
            if current_id != user_id:
                distance_sum += dist

            # Get connections
            current_user = self._users[current_id]
            for friend_id in current_user.get_connections():
                if friend_id not in visited:
                    queue.append((friend_id, dist + 1))

        # Step 4: Apply the closeness formula
        if distance_sum == 0:
            return 0.0  # Avoid division by zero if it's a single user

        closeness_value = (total_users - 1) / distance_sum
        return closeness_value

sn = SocialNetwork("SDNet")

# Create some users
sn.create_user("u1", "Alice")
sn.create_user("u2", "Bob")
sn.create_user("u3", "Charlie")
sn.create_user("u4", "Diana")
sn.create_user("u5", "Eve")

# Add relationships
sn.add_relationship("u1", "u2")  # Alice <-> Bob
sn.add_relationship("u2", "u3")  # Bob <-> Charlie
sn.add_relationship("u3", "u4")  # Charlie <-> Diana

# Check degrees
print(sn.connexion_degree("u1", "u2"))  # 1
print(sn.connexion_degree("u1", "u3"))  # 2
print(sn.connexion_degree("u1", "u4"))  # 3
print(sn.connexion_degree("u1", "u5"))  # -1 (not connected)

# Check close network
print(sn.get_close_network("u1"))  # Should show: {'u2', 'u3', 'u4'}

print("Closeness of u1:", sn.closeness("u1"))
print("Closeness of u2:", sn.closeness("u2"))
print("Closeness of u3:", sn.closeness("u3"))
print("Closeness of u4:", sn.closeness("u4"))