  ამ დავალებისთვის თავიდან QT Designer-ში შევქმენი login-ფორმის დიზაინი და შემდეგი ბრძანებით:
pyuic5 -x login.ui -o login.py შევქმენი შესაბამისი პითონის ფაილი და კლასი.

  შემდეგ გავუწერე ვალიდაციები თითოეულ ფილდს რომელიც შეგიძლიათ იხილოთ login მეთოდში.
ასევე გავუწერე ლოგიკა რომელიც, თუ შეყვანილი username და password ემთხვევა ჩვენს მიერ
ჩაჰარდკოდებულ მონაცემებს, გადაგვამისამართებს ახალ ფანჯარაზე რომელიც გვეუბნება: 
"Congratulations! You logged in successfully!"
