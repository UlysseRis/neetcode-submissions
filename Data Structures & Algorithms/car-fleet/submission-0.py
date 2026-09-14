class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(
            zip(position, speed),
            key=lambda car: car[0],
            reverse=True
        )

        stack = []

        for pos, car_speed in cars:
            time = (target - pos) / car_speed

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)