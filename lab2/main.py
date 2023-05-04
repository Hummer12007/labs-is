from lab2.knowledge_system import KnowledgeSystem


def user_interface():
    ks = KnowledgeSystem()

    while True:
        print("\nOptions:")
        print("1. Add person")
        print("2. Add relation")
        print("3. Add rule")
        print("4. Query relation")
        print("5. Exit")

        option = input("\nEnter your choice (1-5): ")

        if option == '1':
            person = input("Enter the person's identifier: ")
            ks.add_person(person)
            print(f"Person {person} added.")

        elif option == '2':
            person1 = input("Enter the first person's identifier: ")
            person2 = input("Enter the second person's identifier: ")
            relation = input("Enter the relation: ")
            ks.add_relation(person1, person2, relation)
            print(f"Relation '{relation}' added between {person1} and {person2}.")

        elif option == '3':
            relation1 = input("Enter the first relation: ")
            relation2 = input("Enter the second relation: ")
            result_relation = input("Enter the resulting relation: ")
            ks.add_rule(relation1, relation2, result_relation)
            print(f"Rule added: {relation1} + {relation2} -> {result_relation}")

        elif option == '4':
            person1 = input("Enter the first person's identifier: ")
            person2 = input("Enter the second person's identifier: ")
            relation = ks.get_relation(person1, person2)
            if relation:
                print(f"The relation between {person1} and {person2} is '{relation}'.")
            else:
                print(f"No relation found between {person1} and {person2}.")

        elif option == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    user_interface()
