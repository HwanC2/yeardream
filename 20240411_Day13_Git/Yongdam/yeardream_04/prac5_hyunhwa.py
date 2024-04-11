# prac5.py

# 동물원 클래스
class Zoo:
    # 생성자
    def __init__(self):
        # 동물들을 저장할 리스트 생성
        self.animals = []

    # 동물 추가 메서드
    def add_animal(self, animal):
        # 동물 리스트에 추가
        self.animals.append(animal)

    # 동물 출력 메서드
    def show_animals(self):
        print('현재 동물원에는 다음 동물들이 있습니다 :')

        # 동물 목록 길이 만큼 반복
        for animal in self.animals :
            print(f'- {animal.name} the {animal.species}')

    # 동물 종류 검색
    def show_animals_by_species(self, species) :
        print(f'{species} 종류의 동물을 출력합니다.')

        # 동물 목록 길이 만큼 반복
        for animal in self.animals :
            # 동일한 동물을 찾았을 때
            if animal.species == species :
                # 해당 동물 출력
                print(f'- {animal.name} the {animal.species}')

# 동물 클래스
class Animal:
    # 생성자(동물이름, 동물 종류)
    def __init__(self, name, species):
        self.name = name        # 동물 이름
        self.species = species  # 동물 종류

def main():
    # 동물원을 선언하고 10마리의 동물들을 추가합니다.
    zoo = Zoo()
    zoo.add_animal(Animal("Leo", "Lion"))
    zoo.add_animal(Animal("Harry", "Hippo"))
    zoo.add_animal(Animal("Ella", "Elephant"))
    zoo.add_animal(Animal("Gerry", "Giraffe"))
    zoo.add_animal(Animal("Gira", "Giraffe"))
    zoo.add_animal(Animal("Terry", "Lion"))
    zoo.add_animal(Animal("Barry", "Bear"))
    zoo.add_animal(Animal("Larry", "Leopard"))
    zoo.add_animal(Animal("Cary", "Crocodile"))
    zoo.add_animal(Animal("Mary", "Monkey"))

    # 동물원에 있는 모든 동물을 출력합니다.
    zoo.show_animals()
    ## 출력 결과 : 
    '''
    현재 동물원에는 다음 동물들이 있습니다 :
    - Leo the Lion
    - Harry the Hippo
    - Ella the Elephant
    - Gerry the Giraffe
    - Gira the Giraffe
    - Terry the Lion
    - Barry the Bear
    - Larry the Leopard
    - Cary the Crocodile
    - Mary the Monkey
    '''

    # 특정 종에 해당하는 동물들의 이름만 출력합니다.
    zoo.show_animals_by_species("Lion")
    # 출력 결과 : 
    '''
    - Leo the Lion
    - Terry the Lion
    '''
    zoo.show_animals_by_species("Elephant")
    # 출력 결과 : 
    '''
    - Ella the Elephant
    '''

    # 이미 존재하는 동물을 추가한 경우, 해당 동물이 이미 있음을 출력합니다.
    zoo.add_animal(Animal("Leo", "Lion"))
    # 출력 결과 : 
    '''
    "Leo the Lion"은 이미 동물원에 있습니다. 다른 이름을 사용하거나, 다른 종으로 추가해주세요.
    '''

if __name__ == "__main__":
    main()
