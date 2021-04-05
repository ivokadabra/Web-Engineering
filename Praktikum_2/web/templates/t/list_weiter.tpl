 <%inherit file="w.tpl"/>
 
   <table>
     <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
        
         
      </tr>
    % for key_s in data_o:
      <tr class="customTable">
         <td>${data_o[key_s][0]}</td>
         <td>${data_o[key_s][1]}</td>
         <td>${data_o[key_s][2]}</td>
         <td>${data_o[key_s][3]}</td>
         <td>${data_o[key_s][4]}</td>
         <td>${data_o[key_s][5]}</td>
         
         
        
         
         <td><a href="/edit_2/${key_s}">bearbeiten</a></td>
         <td><a href="/delete_2/${key_s}" class='clDelete'>Löschen</a></td>
         <td><a href="/anzeigen_weit/${key_s}/${data_o[key_s]}">anzeigen</a></td>
        
      </tr>
      % endfor
   </table>
   <div>
      <a href="/add2">erfassen</a>
   </div>
    <div>
      <a href="/index">zurück</a>
   </div>
  