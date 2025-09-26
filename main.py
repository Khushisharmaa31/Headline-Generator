from headline_generator import HeadlineGenerator

def main():
    generator = HeadlineGenerator()
    print("Synthetic Headlines Generator\n")

    for i in range(5):  # Generate 5 headlines
        print(f"{i+1}. {generator.generate_headline()}")

if __name__ == "__main__":
    main()
