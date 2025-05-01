class CatController:
    def __init__(self):
        pass

    def hourly_run(self, hour):
        hours_check = {8: "1 mouse", 12: "1 hamster", 17: "1 chicken"}
        message = ''

        # Check if cat cage should be opened at 7
        if hour == 7:
            return 'Open cat cage.'

        # Check if water should be given
        if 8 <= hour <= 11 or 13 <= hour <= 19:
            message += "Give water."

        # Check if cat should be fed
        if hour in hours_check:
            if message:
                message += " "  # Add space between messages
            message += f"Feed {hours_check[hour]}"  # Include the specific food item
        
        # Check if the cat cage should be closed at 20
        if hour == 20:
            return 'Close cat cage.'

        # If any message was generated, return it
        if message:
            return message
        else:
            return "Hour is not for giving water."
