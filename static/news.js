// document.addEventListener('DOMContentLoaded', function() {
//     const container = document.getElementById('news-container');

//     fetch('/api/news/')
//         .then(response => response.json())
//         .then(data => {
//             data.forEach(news => {
//                 const newsItem = document.createElement('div');
//                 newsItem.className = 'news-item';
                
//                 if (news.image) {
//                     const img = document.createElement('img');
//                     img.src = news.image;
//                     img.alt = news.title;
//                     newsItem.appendChild(img);
//                 }

//                 const title = document.createElement('h2');
//                 title.textContent = news.title;
//                 newsItem.appendChild(title);

//                 const summary = document.createElement('p');
//                 summary.textContent = news.summary;
//                 newsItem.appendChild(summary);

//                 container.appendChild(newsItem);
//             });
//         })
//         .catch(error => {
//             console.error('Error fetching news:', error);
//             container.innerHTML = "<p>Unable to load news at this time.</p>";
//         });
// });
