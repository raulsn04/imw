<html>

  <head>
    <meta charset="utf-8">
  </head>

  <body>

    <table border = "20px solid black">

      <?php
          if (isset($_GET["filas"]) and isset($_GET["columnas"])) {

          $columnas = (int) $_POST["columnas"];
          $filas = (int) $_POST["filas"];

          if ($filas < 1 or $columnas < 1) {
            echo ("Entrada erronea");
          }

          else {
            for ($filas = 1; $filas <= $filas; $filas++){
              echo ("<tr>\n");
              for ($columnas = 1, $columnas <= $columnas; $columnas++){
                echo ("<td></td>\n");
              }
              echo ("</tr>\n");
            }
          }
          }
          ?>
      </table>
    </body>
</html>
