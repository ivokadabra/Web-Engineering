## coding: utf-8
<!DOCTYPE html>
<html>
   <head>
      <title>Web-Teams</title>
      <meta charset="UTF-8" />
      <script type="text/javascript" src="/webteams.js"></script>
   </head>
   <body>
      <%
         nr_i = 0
      %>
      <ul>
         % for key_s in data_o:
         <%
            nr_i += 1
         %>
         <li>Team ${nr_i}:
            <a href="/edit/${key_s}/${listform0}/">bearbeiten</a>
            <a href="/delete/${key_s}">Löschen</a>
            <ul>
               <li>${data_o[key_s][0]}, ${data_o[key_s][1]}, ${data_o[key_s][2]}</li>
               <li>${data_o[key_s][0]}, ${data_o[key_s][1]}, ${data_o[key_s][2]}</li>
            </ul>
         </li>
         % endfor
      </ul>
      <div>
         <a href="/add/${listform0}/">erfassen</a>
      </div>
      <div>
         <a href="/?listform=${listform}">Als ${listformText} darstellen</a>
      </div>
   </body>
</html>