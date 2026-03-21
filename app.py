from flames import calculate_flames

def main():
    print(" FLAMES Calculator \n")
    
    name1 = input("Enter your name: ")
    name2 = input("Enter your partner name: ")
    
    try:
        result = calculate_flames(name1, name2)
        
        print("\n Results:")
        print(f"Name 1: {result['name1']} (Length: {result['length1']})")
        print(f"Name 2: {result['name2']} (Length: {result['length2']})")
        print(f"\n Relationship: {result['result']}")
    
    except Exception as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    main()