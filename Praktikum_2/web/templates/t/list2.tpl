
 <%inherit file="w.tpl"/>

    <% nr_i = 0 %>
    % for key_s in data_o:
    <ul class="customTable"> <br> <% nr_i += 1 %>
        <li>Team ${nr_i}:
            <a href="/edit/${key_s}">bearbeiten</a> <br>
            <ul>
               <li>Name: ${data_o[0]}, Vorname: ${data_o[1]}, Matr.-Nr.: ${data_o[2]} , Semester : ${data_o[3]} </li>
               <li>Name: ${data_o[4]}, Vorname: ${data_o[5]}, Matr.-Nr.: ${data_o[6]} , Semester : ${data_o[7]} </li>
            <ul>
        </li>
    </ul>
    % endfor

    <div> <a href="/add2">erfassen</a> </div>
    <div> <a href="/index_2">Auf andere Weise darstellen</a> </div>
