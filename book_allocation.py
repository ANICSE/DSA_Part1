def book_allocation(books, students):
    if students > len(books):
        return False
    
    low = max(books)
    high = sum(books)

    result = high
    while low <=high:
        mid = (low + high) //2
        if is_possible(books, students, mid):
            result = mid
            high = mid - 1 # search  in left
        else:
            low = mid + 1
        
    return result

def is_possible(books, students, max_pages):
    count = 1
    page_sum = 0
    for pages in books:
        if pages > max_pages:
            return False #One book has more pages than the allowed max
        
        if pages + page_sum <= max_pages:
            page_sum += pages
        else:
            count +=1  ##allocate to a new student
            page_sum = pages
    return count <=students

def main():
    books = [12, 34, 67, 90]
    student = 2
    result = book_allocation(books, student)
    print(f"Minimum of the maximum pages a student has to read: {result}")

if __name__ =="__main__":
    main()