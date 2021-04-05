 <%inherit file="w.tpl"/>
   



   <table>
       
       <tr class="customTable">
         <th>Abschlossen</th>
        </tr>

      
      <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
         
      </tr>
       % for i in range(o):
      <tr class="customTable">
         <td>${data_a[i][0]}</td>
         <td>${data_a[i][1]}</td>
         <td>${data_a[i][2]}</td>
         <td>${data_a[i][3]}</td>
         <td>${data_a[i][4]}</td>
         <td>${data_a[i][5]}</td>
        <td><a href="/zeige_mit/${data_a[i]}">zeige Mitarbeiter</a></td>
       
         
      </tr>

     %endfor




        <tr class="customTable">
         <th>Laufende</th>
        </tr>

      
      <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
         
      </tr>
       % for i in range(ip):
      <tr class="customTable">
         <td>${data_o[i][0]}</td>
         <td>${data_o[i][1]}</td>
         <td>${data_o[i][2]}</td>
         <td>${data_o[i][3]}</td>
         <td>${data_o[i][4]}</td>
         <td>${data_o[i][5]}</td>
        <td><a href="/brechen/${data_o[i]}/">anbrechen</a></td>
         
      </tr>

     %endfor


       <tr class="customTable">
         <th>Geplanten</th>
        </tr>

      
      <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
         
      </tr>
      % for i in range(id):
      <tr class="customTable">
         <td>${data_u[i][0]}</td>
         <td>${data_u[i][1]}</td>
         <td>${data_u[i][2]}</td>
         <td>${data_u[i][3]}</td>
         <td>${data_u[i][4]}</td>
         <td>${data_u[i][5]}</td>
       
         
      </tr>
      
     %endfor

    </table>
  
