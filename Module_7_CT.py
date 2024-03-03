def create_course_room_dict():
    return {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

def create_course_instructors_dict():
    return {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

def create_course_meeting_times_dict():
    return {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

def main():
    # Create dictionaries
    course_room_dict = create_course_room_dict()
    instructors_dict = create_course_instructors_dict()
    meeting_times_dict = create_course_meeting_times_dict()

    # Get course number input from user
    course_number = input("Enter the course number: ")

    # Display information
    if course_number in course_room_dict:
        room_number = course_room_dict[course_number]
        instructor = instructors_dict[course_number]
        meeting_time = meeting_times_dict[course_number]

        print(f"Room Number: {room_number}")
        print(f"Course Instructor: {instructor}")
        print(f"Course Meeting Time: {meeting_time}")
    else:
        print("Course not found.")

if __name__ == "__main__":
    main()