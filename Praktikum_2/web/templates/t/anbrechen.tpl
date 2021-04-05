
     <%inherit file="w.tpl"/> 
   <table>
      <tr class="customTable">
         <th>Name (1)</th>
         <th>Vorname (1)</th>
         <th>Akademische Grade (1)</th>
         <th>Tätigkeit (1)</th>
         
      </tr>
      % for key_s in range(i):
      <tr class="customTable">
         <td>${data_o[key_s][0]}</td>
         <td>${data_o[key_s][1]}</td>
         <td>${data_o[key_s][2]}</td>
         <td>${data_o[key_s][3]}</td>
         <td><a href="/change_status/${key_s}/${data_u}/${3}/${data_o[key_s]}">anbrechen</a></td>
       
      % endfor
   </table>
   <div>
      <a href="/add">erfassen</a>
   </div>
    <div>
      <a href="/weit">zurück</a>
   </div>
