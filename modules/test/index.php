<?php
$servername = "localhost";
$username = "root";

$password = "";
$dbname = "andhernagri";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);


// Check connection
if ($conn->connect_error) {
    header("location:connection_error.php?error=$conn->connect_error");
   
 die($conn->connect_error);
}
// Get the category parameter from the URL
$category = $_GET['category'];

// Simulate a vulnerable SQL query
$query = "SELECT * FROM services WHERE `category_id` = '$category";
$result = mysqli_query($connection, $query);

// Process the query result
if ($result) {
    while ($row = mysqli_fetch_assoc($result)) {
        echo $row['product_name'] . "<br>";
    }
} else {
    echo "Error executing the query";
}

?>
