#!/usr/bin/env python


class Aquarium:
    def __init__(this, FISHCOUNT, EyeColor, skinColor):
        this.SkinColor = skinColor
        this.PRIVATE_SWIM_COUNT = 0
        this.EYECOLOR = EyeColor
        this.protected_DEAD_FISH = 0
        this.fishCount = FISHCOUNT

    def start(those):
        if those.fishCount == 0:
            print("There are no alive fish left.")
            return
        those.PRIVATE_SWIM_COUNT += 1

        print(
            str(those.fishCount)
            + " fish are swimming. Their eyes are "
            + those.EYECOLOR
            + " and their skin is "
            + those.SkinColor
            + "."
        )
        print(
            "There are "
            + str(those.protected_DEAD_FISH)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(those.PRIVATE_SWIM_COUNT)
            + " times."
        )

    def kill_fish(__that, _number):
        if __that.fishCount == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        __that.fishCount -= _number
        __that.protected_DEAD_FISH += _number
        if _number > 1:
            print(str(_number) + " fish have died.")
        else:
            print("A fish has died.")


if __name__ == "__main__":
    MyAquariumApp = aquarium_app(5, "blue", "red")
    MyAquariumApp._start()
    MyAquariumApp._aquarium_app__die_fish(2)
    MyAquariumApp._start()
    MyAquariumApp._aquarium_app__die_fish(1)
    MyAquariumApp._start()
    MyAquariumApp._aquarium_app__die_fish(2)
    MyAquariumApp._start()
    MyAquariumApp._aquarium_app__die_fish(1)
