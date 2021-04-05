 <%inherit file="w.tpl"/>
   



   <table>
       
        <tr class="customTable">
         <th>Zukunftige</th>
        </tr>

      
      <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
          
        
         
      </tr>
      % for z in range(opa):
      <tr class="customTable">
         <td>${data_o[z][0]}</td>
         <td>${data_o[z][1]}</td>
         <td>${data_o[z][2]}</td>
         <td>${data_o[z][3]}</td>
         <td>${data_o[z][4]}</td>
         <td>${data_o[z][5]}</td>
       
        
         
      </tr>
      %endfor



       <tr class="customTable">
         <th>An dennen man teilnehmen wird</th>
        </tr>

     
      <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
         <th>Status (1)</th>
     </tr>


      % for j in range(p):
      <tr class="customTable">
         <td>${data_u[j][0]}</td>
         <td>${data_u[j][1]}</td>
         <td>${data_u[j][2]}</td>
         <td>${data_u[j][3]}</td>
         <td>${data_u[j][4]}</td>
         <td>${data_u[j][5]}</td>
         <td>${pp[j]}</td>
         <td><a href="/status_alt/${data_u[j]}/${nomer}">stonieren</a></td>
         
      </tr>
    %endfor

    </table>
  
    <div>
      <a href="/mitarbeiter">zurück</a>
   </div>
