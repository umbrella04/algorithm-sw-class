# 단순연결구조를 위한 Node 클래스
class Node:
    def __init__(self,elem,link=None):
        self.data = elem # 데이터 필드
        self.link = link # 링크 필드

    def append(self, new):
        # 현재 노드 (self) 뒤에 새로운 노드 (new)를 추가하는 연산
        if new is not None:
            new.link = self.link
            self.link = new 

    def popNext(self): 
        # 현재 노드의 다음 노드를 리스트에서 제거하고, 그 노드를 반환
        deleted = self.link
        if deleted is not None:
            self.link = deleted.link
            deleted.link = None # 연결 해제
        return deleted 


# 단순연결리스트 클래스
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self) :
        # 리스트가 비어있는지 검사
        return self.head == None

    def isFull(self):
        # 리스트의 포화상태 검사
        return False
    
    def getNode(self, pos):
        # pos번째에 있는 노드를 반환하기
        # 리스트의 인덱스는 0부터 시작
        if pos < 0 : return None # pos는 invalid 졍우
        if self.head == None: # 주어진 리스트가 공백
            return None
        else:
            ptr  = self.head
            for _ in range(pos):
                if ptr == None: # pos가 리스트 크기보다 큰 경우 
                    return None
                ptr = ptr.link # 링크따라 이동
            return ptr #pos에 있는 노드 반환
        
    def getEntry(self, pos):
        # 리스트의 pos 위치에 있는 노드의 데이터를 반환
        node = self.getNode(pos) # getNode() 를 이용하여 pos 위치에 있는 노드 먼저 찾기
        if node == None:
            return None
        else :
            return node.data
        
    def insert(self,pos,elem):
        # 리스트의 pos 위치에 새로운 노드를 추가
        if pos < 0 : return # 자동으로 유효하지않는 위치에 대해 ValueError 발생

        new = Node(elem) # 또는 Node(elem, None) # 1. 새 노드 생성
        before = self.getNode(pos-1) # 2. pos-1 위치의 노드를 가져오기
        # 3. before 노드의 위치에 따라 구분
        if before is None:
            if pos == 0 :# 1) 머리 노드로 삽입
                new.link = self.head
                self.head = new
                return
            else: # 2)pos가 리스트의 범위를 벗어나는 경우
                raise IndexError(" 리스트 밖에 있는 위치")
        else: # 3) 중간노드로 삽입
            before.append(new) # before 노드 뒤에 삽입

    def delete(self, pos):
        # 리스트에 pos 위치에 있는 노드 삭제한고 반환
        if pos < 0 : 
            raise IndexError("empty 또는 리스트 범위 밖 오류")
        
        before = self.getNode(pos-1) # 1. 삭제할 노드 이전 노드 
        # 2. before 노드의 위치에 따라 구분
        if before == None:
            if pos == 0 : # 1)머리 노드 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None # 연결 해제
                return deleted
            else: #  2)pos가 리스트 밖에 있는 경우
                raise ValueError("리스트 범위 밖 오류")
        else: 
            before.popNext() # #3) 중간 노드로 삭제 

    def size(self):   
        # 리스트의 전체 노드의 개수 구하기
        if self.head == None : # 리스트가 빈 경우
            return 0        
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.link
            return count 
    
    def display(self, msg = "LinkedList:"):
        print(msg, end = ' ')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '->')
            ptr = ptr.link
        print("None")

    def replace(self, pos, elem):
        node = self.getNode(pos) 
        if node != None:
            node.data = elem
        else: 
            return 
        
    def find_by_title(self, title): 
        pos = 0
        while pos < self.size():
            book = self.getEntry(pos)
            if title == book.title:
                return book
            pos += 1
        return None
    
    def find_pos_by_title(self, title):
        pos = 0
        while pos < self.size():
            book = self.getEntry(pos)
            if title == book.title:
                return pos
            pos += 1
        return None

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
    
    def display_book(self):
        print(f"[책 번호:{self.book_id}, 제목:{self.title}, 저자:{self.author}, 출판 연도:{self.year}]")


class BookManagement:
    def __init__(self):
        self.list = LinkedList()
    def add_book(self, book_id, title, author, year):
        new = Book(book_id, title, author, year)
        self.list.insert(self.list.size(),new)
    def remove_book(self, title): 
        delete_pos = self.list.find_pos_by_title(title)
        if not delete_pos is None:
            self.list.delete(delete_pos)
            return delete_pos
        else:
            return None
    def search_book(self, title):
        book = self.list.find_by_title(title)
        if not book is None:
            book.display_book()
            return book
        else:
            print("책을 찾지 못했습니다.")
            return None
    def display_books(self):
        ptr = self.list.head
        if ptr is None:
            print("책을 찾지 못했습니다.")
            return
        while not ptr is None:
            ptr.data.display_book()
            ptr = ptr.link
    def run(self):

        while True:
            p = False
            print("===도서 관리 프로그램===")
            print("1. 도서 추가")
            print("2. 도서 삭제")
            print("3. 도서 조회")
            print("4. 전체 도서 목록 조회")
            print("5. 종료")

            select = input("메뉴를 선택하세요 : ")

            if select == '1':
                book_id = input("책 번호를 입력하세요 : ")
                if book_id.isdigit() == False:
                    print("숫자를 입력해주세요.")
                    continue
                ptr = self.list.head
                while not ptr is None:
                    if ptr.data.book_id == book_id:
                        print("책 번호가 중복됩니다.")
                        p = True
                        break
                    ptr = ptr.link
                if p:
                    continue
                title = input("책 제목을 입력하세요 : ")
                author = input("저자를 입력하세요 : ")
                year = input("출판 연도를 입력하세요 : ")
                self.add_book(book_id, title, author, year)
                print(f"도서 '{title}'가 추가되었습니다.")
                continue
            elif select == '2':
                delete_title = input("삭제할 책 제목을 입력하세요 : ")
                remove = self.remove_book(delete_title)
                if remove == None:
                    print(f"삭제할 책 '{delete_title}'를 발견하지 못했습니다.")
                    continue
                print(f"책 제목 '{delete_title}'가 삭제되었습니다.")
                continue
            elif select == '3':
                search_title = input("조회할 책 제목을 입력하세요 : ")
                self.search_book(search_title)
            elif select == '4':
                self.display_books()                
            elif select == '5':
                break
            else:
                print("올바른 메뉴를 골라주세요.")

if __name__ == "__main__" :
    book = BookManagement()
    book.run()

    