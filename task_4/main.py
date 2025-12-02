from bs4 import BeautifulSoup
import requests
import json

with open("C:\\Users\\Ryzen 7\\OneDrive\\Desktop\\ipo-lr-11\\task_2\\data.json", "r", encoding='utf-8') as file:
    data = json.load(file)
html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hacker News Parser</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        th, td {
            padding: 12px 15px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #4a6fa5;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        .source-link {
            display: block;
            text-align: center;
            margin-top: 30px;
            padding: 10px;
            background: #4a6fa5;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .source-link:hover {
            background: #3a5a80;
        }
    </style>
</head>
<body>
    <h1>📰 Новости с Hacker News</h1>
    <table>
        <tr>
            <th>№</th>
            <th>Заголовок</th>
            <th>Комментарии</th>
        </tr>'''
    
for i, item in enumerate(data, 1):
    html += f'''
        <tr>
            <td>{i}</td>
            <td>{item.get('Title', '')}</td>
            <td>{item.get('Comments', '')}</td>
        </tr>'''
    
html += '''
    </table>
    <a href="https://news.ycombinator.com/" target="_blank" class="source-link">
        🔗 Перейти на оригинальный сайт Hacker News
    </a>
</body>
</html>'''
    
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("HTML страница создана!")

