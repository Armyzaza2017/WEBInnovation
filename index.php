<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SummarizeBot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        p {
            margin-bottom: 20px;
            line-height: 1.6;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .btn:hover {
            background-color: #0056b3;
        }
        nav {
            background-color: #333;
            color: #fff;
            padding: 10px 20px;
            text-align: center;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin-right: 20px;
        }
    </style>
</head>
<body>
    <nav>
        <a href="home.php">Home</a>
        <a href="templates/indexPDF.php">PDF Summary</a>
        <a href="templates/indexTXT.php">TXT Summary</a>
        <a href="templates/indexWEB.php">Website Summary</a>
    </nav>
    <div class="container">
        <h1>Welcome to SummarizeBot</h1>
        <p>SummarizeBot is an online tool that helps you summarize the content of PDF files and text files (TXT) automatically. It's fast, accurate, and easy to use.</p>
        <p>To start summarizing, simply upload your PDF or text file and let SummarizeBot do the rest!</p>

    </div>
</body>
</html>
