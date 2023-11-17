class RealProperty:
    def __init__(
        self, rooms: int, square_meters: int, price_per_sqm: int, description: str
    ):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, self2):
        return self.square_meters > self2.square_meters

    def price_difference(self, self2):
        # Function abs returns absolute value
        difference = abs(
            (self.price_per_sqm * self.square_meters)
            - (self2.price_per_sqm * self2.square_meters)
        )
        return difference

    def more_expensive(self, self2):
        difference = (self.price_per_sqm * self.square_meters) - (
            self2.price_per_sqm * self2.square_meters
        )
        return difference > 0

    def __repr__(self):
        return (
            f"RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, "
            + f"price_per_sqm = {self.price_per_sqm}, description = {self.description})"
        )


# WRITE YOUR SOLUTION HERE:
def cheaper_properties(properties: list, reference: RealProperty):
    return [
        f"{item.description:35} price difference {item.price_difference(reference)} euros"
        for item in properties
        if item.price_per_sqm * item.square_meters
        < reference.square_meters * reference.price_per_sqm
    ]


if __name__ == "__main__":
    a1 = RealProperty(1, 16, 5500, "Central studio")
    a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
    a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
    a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
    a5 = RealProperty(4, 105, 1700, "Loft in a small town")
    a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

    properties = [a1, a2, a3, a4, a5, a6]

    print(f"cheaper options when compared to {a3.description}:")
    for item in cheaper_properties(properties, a3):
        print(item)

    # print(cheaper_properties([RealProperty(1, 1, 1, "a")], RealProperty(1, 1, 2, "b")))
