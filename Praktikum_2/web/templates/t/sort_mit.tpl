 <%inherit file="w.tpl"/>
     
   <table>
      <tr class="customTable">
         <th>Name (1)</th>
         <th>Vorname (1)</th>
         <th>Akademische Grade (1)</th>
         <th>Tätigkeit (1)</th>
         
      </tr>
      % for key_s in range(length):
      <tr class="customTable">
         <td>${data_o[key_s][1]}</td>
         <td>${data_o[key_s][0]}</td>
        
         <td>${data_o[key_s][2]}</td>
         <td>${data_o[key_s][3]}</td>
         <td><a href="/sort_mit_weit/${data_o[key_s]}">Hronologissch Weiterbildung zeigen</a></td>
         
      </tr>
      % endfor
   </table>
   
    <div>
      <a href="/index">zurück</a>
   </div>
 