<?php 
    $errorcodes = array("418", "450", "451", "426", "508", "420", "527", "100", "406", "69")
?>
<div class="errorrorrrrrr">
    Error
    <?php
    if ($_SERVER['REQUEST_URI'] == '/error_418.php') {
        echo "418";
    } else {
        echo $errorcodes[array_rand($errorcodes)];
    }
    ?>

</div>
