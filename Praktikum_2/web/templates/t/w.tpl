<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Side Navigation Bar</title>
   
    <style>
    @import "/webteams.css";
    @import "/styles.css";
    </style>
    <script type="text/javascript" src="webteams.js"></script>
	
</head>
<body>

<div id="myNavbar" class="wrapper">
    <div class="sidebar">
        <h4>Mitarbeiterqualifizierung</h4>
        <ul>
            <li><a href="/index_2"><i class="fas fa-home"></i>Pflege Mitarbeiter</a></li>
            <li><a href="/index_3"><i class="fas fa-user"></i>Pflege Weiterbildung</a></li>
            <li>Teilname</li>
            <li><a href="/mitarbeiter"><i class="fas fa-blog"></i>Sichtweise Mitarbeiter</a></li>
            <li><a href="/weit"><i class="fas fa-address-book"></i>Sichtweise Weiterbildung</a></li>
             <li>Auswertung</li>
            <li><a href="/sort_mitarbeiter"><i class="fas fa-blog"></i>Mitarbeiter</a></li>
            <li><a href="/sort_weiterbildung"><i class="fas fa-address-book"></i>Weiterbildung</a></li>
             <li><a href="/sort_zertifikate"><i class="fas fa-address-book"></i>Zertifikate</a></li>
        </ul> 
        
    </div>
    <div class="main_content">
        <div class="header">Ivaylo Iliev.</div>  
        <div class="info"></div>
    </div>
   
</div> 
<div class="box">
${self.body()}
</div>
</body>
</html>