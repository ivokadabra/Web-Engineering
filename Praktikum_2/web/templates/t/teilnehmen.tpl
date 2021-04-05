 <%inherit file="w.tpl"/>

   



   <table>
      <tr class="customTable">
         <th>Name (1)</th>
         <th>Vorname (1)</th>
         <th>Akademische Grade (1)</th>
         <th>Tätigkeit (1)</th>
         
      </tr>
    
      <tr class="customTable">
         <td>${data_o[0]}</td>
         <td>${data_o[1]}</td>
         <td>${data_o[2]}</td>
         <td>${data_o[3]}</td>
         <td><a href="/sta/${id}">anbrechen</a></td>
         
      </tr>
     
   </table>
   <div>
      <a href="/add">erfassen</a>
   </div>
    <div>
      <a href="/index">zurück</a>
   </div>
