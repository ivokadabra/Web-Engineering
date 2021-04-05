
 <%inherit file="w.tpl"/>
   
     
   <table>
      <tr class="customTable">
         <th>Zertifikate Beschreibung</th>
         <th>Zertifikate Bezeichnung</th>
       
         
      </tr>
      % for key_s in range(length):
      <tr class="customTable">
         <td>${data_o[key_s][6]}</td>
         <td>${data_o[key_s][7]}</td>
         
      
         
      </tr>
      % endfor
   </table>
   
    <div>
      <a href="/index">zurück</a>
   </div>
