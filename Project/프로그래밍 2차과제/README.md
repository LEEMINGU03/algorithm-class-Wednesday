## 핵심 구현

* **`Node`**: `Book` 객체를 `data`로 갖고, 다음 노드를 가리키는 `link`를 가진 노드 클래스
* **`Book`**: 도서 정보(`bookID`, `title`, `author`, `year`)를 저장하는 데이터 클래스
* **`LinkedList`**: `Node`들을 관리하며 `insert`, `delete`, `getNode`, `size` 등의 기본 연산 제공
* **`BookManagement`**: `LinkedList`를 사용하여 도서 관리 로직과 메뉴(`run`)를 실행


## 시간 복잡도 분석
**도서 추가 (Add Book): $O(n)$**
**도서 삭제 (Remove Book): $O(n)$**
**도서 조회 (Search Book): $O(n)$**
**전체 목록 출력 (Display All): $O(n)$**