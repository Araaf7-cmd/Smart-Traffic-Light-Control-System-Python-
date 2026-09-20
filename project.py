
import time
import random

responses = {
    "hi": [
        "Hello!  Welcome to our University Enquiry Chatbot.",
        "Hi there!  How can I help you with university information today?"
    ],
    "hello": [
        "Hey! Hope you're doing great. What would you like to know about our university?",
        "Hello! How can I assist you today?"
    ],
    "admission": [
        "Admissions are open! You can apply online through the official university website.",
        "Our admission process is fully online. Visit the university portal to register and apply.",
        "Admission forms are available on our website. Make sure to check eligibility and deadlines!"
    ],
    "courses": [
        "We offer undergraduate and postgraduate programs such as B.Tech, BBA, MBA, and M.Tech.",
        "Our university provides a wide range of courses in Engineering, Management, and Sciences.",
        "Popular programs include B.Tech in CSE, Mechanical, Civil, and Electrical Engineering."
    ],
    "fees": [
        "The fee structure varies by program. You can download the detailed fee brochure from our website.",
        "Tuition fees depend on the course and specialization. Please visit the Admissions > Fee Structure section online.",
        "You can contact the Accounts Department for the latest fee details and payment options."
    ],
    "hostel": [
        "Yes, hostel facilities are available for both boys and girls with 24/7 security and Wi-Fi.",
        "Our hostels provide comfortable rooms, healthy meals, and a safe environment for all students.",
        "The university offers both AC and Non-AC hostel options depending on your preference."
    ],
    "placements": [
        "Our Placement Cell has strong ties with companies like Infosys, TCS, Wipro, and Deloitte.",
        "We have an excellent placement record, with top recruiters visiting the campus every year.",
        "Students are trained in soft skills, resume building, and interview preparation for better placements."
    ],
    "library": [
        "The central library houses thousands of books, journals, and digital resources.",
        "Our library is open from 9 AM to 8 PM on weekdays and 10 AM to 5 PM on weekends.",
        "Students can access e-books and research papers through the university digital library portal."
    ],
    "canteen": [
        "We have multiple canteens and food courts offering affordable, hygienic, and tasty food.",
        "Our canteen serves a variety of cuisines to cater to diverse student preferences.",
        "Healthy and budget-friendly meals are available across campus dining facilities."
    ],
    "sports": [
        "The university offers sports facilities for cricket, football, badminton, basketball, and athletics.",
        "Annual sports events and inter-college tournaments encourage active student participation.",
        "We promote fitness through indoor and outdoor sports facilities for all students."
    ],
    "scholarships": [
        "Scholarships are available based on academic merit, sports performance, and financial need.",
        "The university offers merit-based scholarships for students with excellent academic records.",
        "You can apply for government and institutional scholarships during the admission process."
    ],
    "thank you": [
        "You're most welcome! Glad I could help.",
        "Happy to assist! If you have more questions, feel free to ask.",
        "You're welcome! Have a great day ahead! "
    ],
    "thanks": [
        "You're welcome! ",
        "Glad to help! ",
        "Anytime! Wishing you all the best with your studies!"
    ],
    "bye": [
        "Goodbye!  Wishing you success in your university journey.",
        "Bye-bye! Take care and best of luck with your admission!",
        "See you soon! Don’t hesitate to come back if you have more queries. "
    ]
}

def find_best_match(user_input):
    """
    Simple keyword-based matching.
    It checks for keywords in user input and returns the best-matching response.
    """
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])
    return None


def chatbot_response(user_input):
    """
    Generates the chatbot's response based on user input.
    """
    reply = find_best_match(user_input)
    if reply:
        return reply
    else:
        return (
            "I'm sorry 😔, I couldn't understand that. "
            "Could you please rephrase or ask about admissions, courses, or facilities?"
        )

def chat():
    print("=" * 60)
    print("🎓  AI-Powered Chatbot for University Enquiries")
    print("=" * 60)
    print("Type 'bye' or 'exit' anytime to end the chat.\n")
    print("Type 'Hi' or 'Hello' to start the chat!")
    time.sleep(1)

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() in ["bye", "exit", "quit"]:
            print("Chatbot:", random.choice(responses["bye"]))
            break

        response = chatbot_response(user_input)
        time.sleep(0.5)
        print("Chatbot:", response)
        print()

# Run the Chatbot
if __name__ == "__main__":
    chat()
