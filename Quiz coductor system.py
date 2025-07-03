import time
import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def show_welcome():
    print("\n" + "="*50)
    print("🌟".center(50))
    print("      Quiz  Conductor".center(50))
    print("🌟".center(50))
    print("="*50 + "\n")
    print("Answer each question by entering 1, 2, 3, or 4".center(50))
    print("Score 80%+ to unlock the 'Tech Guru' title!\n")
    print("Loading questions", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions, 1):
        print(f"\n{' Question ' + str(i) + ' ':-^50}")
        print(question.prompt)
        
        while True:
            user_answer = input(">>> Your answer (1-4): ").strip()
            if user_answer in ['1', '2', '3', '4']:
                break
            print("⚠️ Invalid! Please enter 1, 2, 3, or 4")
        
        if user_answer == question.answer:
            score += 1
            print("\n✅ Correct! " + "✔"*score)
        else:
            print(f"\n❌ Incorrect! Correct answer: {question.answer}")
        
        progress = (i/len(questions))*100
        print(f"\n📊 Progress: {i}/{len(questions)} ({progress:.0f}%)")
    
    return score

def show_result(score, total):
    percentage = (score / total) * 100
    
    print("\n\n" + "="*50)
    print(" QUIZ RESULTS ".center(50, "⚡"))
    print("="*50)
    
    print(f"\n🎯 Your Score: {score}/{total}".center(50))
    print(f"📈 Percentage: {percentage:.1f}%".center(50))
    
    print("\n" + "-"*50)
    if percentage >= 90:
        print("🌟 TECH GENIUS 🌟".center(50))
        print("You're in the top 10% of tech experts!".center(50))
    elif percentage >= 70:
        print("💻 TECH GURU 💻".center(50))
        print("Impressive knowledge!".center(50))
    elif percentage >= 50:
        print("🔧 TECH ENTHUSIAST 🔧".center(50))
        print("Good foundation - keep learning!".center(50))
    else:
        print("📚 TECH APPRENTICE 📚".center(50))
        print("Review these topics and try again!".center(50))
    print("="*50 + "\n")

def main():
    questions = [
        Question("What does 'GPU' stand for?\n1) Graphics Processing Unit\n2) General Processing Unit\n3) Global Processing Unit\n4) Graphical Performance Unit\n", "1"),
        Question("Which language is primarily used for iOS development?\n1) Kotlin\n2) Swift\n3) Java\n4) C#\n", "2"),
        Question("What does 'SSL' stand for?\n1) Secure Sockets Layer\n2) System Security Layer\n3) Server Side Language\n4) Super Secure Login\n", "1"),
        Question("Which company developed the Java language?\n1) Microsoft\n2) Sun Microsystems\n3) Google\n4) Oracle\n", "2"),
        Question("What is the main purpose of Docker?\n1) Version control\n2) Containerization\n3) Virtual machines\n4) Database management\n", "2"),
        Question("What does 'AI' stand for?\n1) Automated Intelligence\n2) Artificial Intelligence\n3) Advanced Interface\n4) Algorithmic Iteration\n", "2"),
        Question("What's the binary equivalent of decimal 10?\n1) 1010\n2) 1001\n3) 1100\n4) 1111\n", "1"),
        Question("Which protocol is used by Bitcoin?\n1) HTTP\n2) FTP\n3) Blockchain\n4) SMTP\n", "3"),
        Question("What does 'IDE' stand for?\n1) Integrated Development Environment\n2) International Development Environment\n3) Integrated Debugging Engine\n4) Internet Development Environment\n", "1"),
        Question("Which data structure uses FIFO principle?\n1) Stack\n2) Queue\n3) Array\n4) Tree\n", "2"),
        Question("What does 'CDN' stand for?\n1) Content Delivery Network\n2) Centralized Data Node\n3) Coded Data Network\n4) Core Distribution Network\n", "1"),
        Question("Which language runs fastest?\n1) Python\n2) JavaScript\n3) C++\n4) PHP\n", "3"),
        Question("What is the purpose of a DNS server?\n1) Host websites\n2) Translate domain names to IPs\n3) Manage emails\n4) Store databases\n", "2"),
        Question("Which technology is primarily used for web styling?\n1) HTML\n2) CSS\n3) JavaScript\n4) Python\n", "2"),
        Question("What does 'SEO' stand for?\n1) Search Engine Optimization\n2) System Execution Order\n3) Security Enhancement Option\n4) Software Engineering Operation\n", "1"),
        Question("Which company created React.js?\n1) Google\n2) Microsoft\n3) Facebook\n4) Apple\n", "3"),
        Question("What type of database is MongoDB?\n1) SQL\n2) NoSQL\n3) Graph\n4) Key-value\n", "2"),
        Question("Which HTTP status code means 'Not Found'?\n1) 200\n2) 301\n3) 404\n4) 500\n", "3"),
        Question("What does 'API' primarily facilitate?\n1) Communication between software components\n2) Graphics rendering\n3) Data storage\n4) User authentication\n", "1"),
        Question("Which architectural pattern separates concerns?\n1) MVC\n2) DBMS\n3) FTP\n4) HTTP\n", "1"),
        Question("What does 'OOP' stand for?\n1) Object-Oriented Programming\n2) Operational Output Protocol\n3) Optimized Organizational Process\n4) Open Office Platform\n", "1"),
        Question("What is the maximum value of an 8-bit integer?\n1) 128\n2) 255\n3) 256\n4) 1024\n", "2"),
        Question("Which protocol encrypts web traffic?\n1) HTTP\n2) HTTPS\n3) FTP\n4) SMTP\n", "2"),
        Question("What does 'VPN' stand for?\n1) Virtual Private Network\n2) Visual Processing Node\n3) Verified Public Network\n4) Virtualized Private Node\n", "1"),
        Question("Which language has garbage collection?\n1) C\n2) Assembly\n3) Python\n4) All of the above\n", "3")
    ]

    # Shuffle the questions
    random.shuffle(questions)

    show_welcome()
    final_score = run_quiz(questions)
    show_result(final_score, len(questions))

if __name__ == "__main__":
    main()
