from bs4 import BeautifulSoup


def parse_email_content_html(email_content: str):
    soup = BeautifulSoup(email_content, 'html.parser')
    text_content = ""

    messages_unquoted = soup.select('div:not(.gmail_quote)')[0]
    for d in messages_unquoted.find_all(['div', 'h1', 'a']):
        text_content += " " + d.get_text(strip=True)
    return text_content


clear_examp = """
<div dir="ltr">Bonjour,
    <div>Merci ! tu le trouveras en pièce jointe.</div>
    <div><br></div>
    <div>Bonne journée,</div>
    <h1>hello fucking world</h1>
    <a href="hello">aywaa</a>

</div><br>
<div class="gmail_quote">
    <a>helloo</a>
</div>
<div><br></div>-- <br>
<div dir="ltr">
    <div dir="ltr">EL HASSANE</div>
</div>
"""

karim = """
<div>
<div>
<div>
<div dir="ltr">
<div>Parfait, tout devrait se passer pour le mieux alors ! </div>
<div dir="ltr"><br>
</div>
<div dir="ltr">J’aurai besoin de quelques renseignements supplémentaires, peut-on convenir d’un rendez vous demain à 16h ? </div>
<div dir="ltr"><br>
</div>
<div dir="ltr">Cordialement </div>
</div>
</div>
<div id="m_8275504812610894377ms-outlook-mobile-signature">
<div></div>
</div>
</div>
<hr style="display:inline-block;width:98%">
<div id="m_8275504812610894377divRplyFwdMsg" dir="ltr"><font face="Calibri, sans-serif" style="font-size:11pt" color="#000000"><b>De :</b> Karim &lt;<a href="mailto:karimo49300@gmail.com" target="_blank">karimo49300@gmail.com</a>&gt;<br>
<b>Envoyé :</b> Saturday, February 18, 2023 2:44:21 PM<br>
<b>À :</b> Karim Benchekroun &lt;<a href="mailto:karimbenchekroun@outlook.fr" target="_blank">karimbenchekroun@outlook.fr</a>&gt;<br>
<b>Objet :</b> Re: Demande de renseignement</font>
<div> </div>
</div>
<div>
<div dir="ltr">D&#39;accord merci, je connais très bien les programmes CCI, j&#39;ai travaillé dessus pendant 3 ans :) 
<div><br>
</div>
<div>Dans l&#39;attente de te lire, </div>
<div><br>
</div>
<div>Karim</div>
</div>
<br>
<div>
<div dir="ltr">Le sam. 18 févr. 2023 à 14:41, Karim Benchekroun &lt;<a href="mailto:karimbenchekroun@outlook.fr" target="_blank">karimbenchekroun@outlook.fr</a>&gt; a écrit :<br>
</div>
<blockquote style="margin:0px 0px 0px 0.8ex;border-left:1px solid rgb(204,204,204);padding-left:1ex">
<div>
<div dir="ltr">
<div></div>
<div>
<div dir="ltr">Hello Karim, pour faire suite à notre discussion de ce matin, je te mets en relation avec Maël Fleuret pour qu&#39;il puisse te parler des programmes CCI qui pourraient te convenir pour le lancement de l&#39;activité de Quinn. D&#39;ici là, si on ouvre des
 postes de travail en open Space, je reviens vers toi ! </div>
<div dir="ltr"><br>
</div>
<div dir="ltr"><br>
</div>
<div dir="ltr"><br>
</div>
<div dir="ltr">Bien à toi, à très vite ! </div>
<div dir="ltr"><br>
</div>
<div dir="ltr"><br>
</div>
<div dir="ltr"><br>
</div>
<div dir="ltr">Laurine Falco</div>
<div id="m_8275504812610894377x_m_-1772224509965191422ms-outlook-mobile-signature" dir="ltr">
<div></div>
</div>
</div>
</div>
</div>
</blockquote>
</div>
</div>
</div>
"""

mm = """
<div dir="ltr">Bonjour Maryem,
    <div><br></div>
    <div>Merci pour cette proposition, malheureusement je ne suis pas à l&#39;écoute du marché actuellement.</div>
    <div><br></div>
    <div>Bien cordialement,</div>
    <div><br></div>
    <div>El hassane</div>
</div><br>
<div class="gmail_quote">
    <div dir="ltr" class="gmail_attr">Le mar. 14 févr. 2023 à 09:20, Maryem EL KHOUMSI &lt;<a
            href="mailto:maryem.elkhoumsi@e3m-management.com" target="_blank">maryem.elkhoumsi@e3m-
        <wbr>
        management.com</a>&gt; a écrit :<br></div>
    <blockquote class="gmail_quote"
                style="margin:0px 0px 0px 0.8ex;border-left:1px solid rgb(204,204,204);padding-left:1ex">
        <div>


            <div dir="ltr">
                <div style="font-family:Calibri,Arial,Helvetica,sans-serif;font-size:12pt;color:rgb(0,0,0);background-color:rgb(255,255,255)">
                    <div style="font-size:15px;margin:0px;color:rgb(36,36,36);background-color:rgb(255,255,255)">
                        <p style="margin:0px;font-size:11pt;font-family:Calibri,sans-serif;background-color:white">
                            <span style="margin:0px"><span
                                    style="font-size:12pt;font-family:Arial,sans-serif;margin:0px;color:rgb(34,34,34)">Bonjour Monsieur GARGEM,</span></span><span
                                style="font-size:12pt;margin:0px;color:black"></span></p>
                    </div>
                    <div style="font-size:15px;margin:0px;color:rgb(36,36,36);background-color:rgb(255,255,255)">
                        <div style="margin:0px">
                            <div style="margin:0px">
                                <div style="margin:0px">
                                    <div style="margin:0px">
                                        <p style="margin:0px 0px 12pt;font-size:11pt;font-family:Calibri,sans-serif;background-color:white">
<span style="font-size:12pt;font-family:Arial,sans-serif;margin:0px;color:rgb(34,34,34)"><br>
<span style="margin:0px"><span style="margin:0px;background-color:white">Comment allez-vous ?</span></span></span><span
                                                style="font-size:12pt;margin:0px;color:black"></span></p>
                                    </div>
                                    <div style="margin:0px">
                                        <p style="margin:0px;font-size:11pt;font-family:Calibri,sans-serif;background-color:white">
                                            <span style="margin:0px"><span
                                                    style="font-size:12pt;font-family:Arial,sans-serif;margin:0px;color:rgb(34,34,34);background-color:white">Je suis Maryem ELKHOUMSI, Consultante en Recrutement chez E-3M une ESN basée en France.</span></span><span
                                                style="font-size:12pt;margin:0px;color:black"></span></p>
                                    </div>
                                    <div style="margin:0px">
                                        <p style="margin:0px;font-size:11pt;font-family:Calibri,sans-serif;background-color:white">
                                            <span style="font-size:12pt;margin:0px;color:black"> </span></p>
                                    </div>
                                    <div style="margin:0px">
                                        <p style="margin:0px;font-size:11pt;font-family:Calibri,sans-serif;background-color:white">
<span style="margin:0px"><span
        style="font-size:12pt;font-family:Arial,sans-serif;margin:0px;color:rgb(34,34,34);background-color:white">Je vous contacte pour savoir si vous êtes à l&#39;écoute du marché et si vous seriez intéressé par
 le poste Développeur Fullstack Python Vuejs ?</span></span><span style="font-size:12pt;margin:0px;color:black"></span>
                                        </p>
                                    </div>
                                    <div style="margin:0px">
                                        <p style="margin:0px;font-size:11pt;font-family:Calibri,sans-serif;background-color:white">
                                            <span style="font-size:12pt;margin:0px;color:black"> </span></p>
                                    </div>
                                    <div style="margin:0px">
                                        <p style="margin:0px;font-size:11pt;font-family:Calibri,sans-serif;background-color:white">
                                            <span style="margin:0px"><span
                                                    style="font-size:12pt;font-family:Arial,sans-serif;margin:0px;color:rgb(34,34,34);background-color:white">Regards,</span></span>
                                        </p>
                                        <p style="margin:0px;font-size:11pt;font-family:Calibri,sans-serif;background-color:white">
<span style="margin:0px"><span
        style="font-size:12pt;font-family:Arial,sans-serif;margin:0px;color:rgb(34,34,34);background-color:white"><br>
</span></span></p>
                                        <div>
                                            <div style="font-family:Calibri,Arial,Helvetica,sans-serif;font-size:12pt;color:rgb(0,0,0)">
                                                <br>
                                            </div>
                                            <div id="m_-8607549945426528868m_-5505950300685995598Signature">
                                                <div>
                                                    <div style="font-family:Calibri,Arial,Helvetica,sans-serif;font-size:12pt;color:rgb(0,0,0);background-color:rgb(255,255,255)">
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <b><span lang="en-US"
                                                                     style="font-size:10pt;font-family:&quot;Century Gothic&quot;,sans-serif,serif,EmojiFont;margin:0px;color:rgb(24,90,161);background-color:white">Maryem ELKHOUMSI - e3M Management</span></b><span
                                                                lang="en-US" style="margin:0px;color:black"></span></p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <span lang="en-US"
                                                                  style="font-size:10pt;font-family:&quot;Century Gothic&quot;,sans-serif,serif,EmojiFont;margin:0px;color:rgb(24,90,161)">Consultante en Recrutement </span><span
                                                                lang="en-US"
                                                                style="font-family:&quot;Segoe UI&quot;,sans-serif,serif,EmojiFont;margin:0px;color:black"></span>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <img alt="Image"
                                                                 style="color:navy;font-family:Arial,sans-serif,serif,EmojiFont;width:114.74pt;height:59.99pt;min-height:auto;min-width:auto"
                                                                 src="https://mail.google.com/mail/?ui=2&amp;ik=f536e26f7d&amp;attid=0.1&amp;permmsgid=msg-a:r-3101072898965362700&amp;th=18650a2ee714ddf9&amp;view=fimg&amp;fur=ip&amp;permmsgid=msg-a:r-3101072898965362700&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ-7CuVYQhXQGFPcI9-wKCFoo876lxTMJt7t142ntkzE2EuCp-5eMmt19sbXjM28LWaHwocyUHea9WgLfCCwiQ0buxqhBjuxy946hGJp4ozE_nN5drnPd-wFEgE&amp;disp=emb&amp;realattid=18650a2325b2d727bf61&amp;zw"
                                                                 data-image-whitelisted><br>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <span style="font-family:&quot;Segoe UI&quot;,sans-serif,serif,EmojiFont;margin:0px;color:black"></span>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <b><u><span
                                                                    style="font-size:9pt;font-family:Verdana,sans-serif,serif,EmojiFont;margin:0px;color:rgb(243,144,29)">______________________________<wbr>__________________________</span></u></b><span
                                                                style="font-family:&quot;Segoe UI&quot;,sans-serif,serif,EmojiFont;margin:0px;color:black"></span>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <b><span
                                                                    style="font-size:9pt;font-family:Candara,sans-serif,serif,EmojiFont;margin:0px;color:rgb(243,144,29)">Email:
<a rel="noopener noreferrer" style="margin:0px">
<span style="margin:0px;color:rgb(5,99,193)">maryem.elkhoumsi@e3m-<wbr>management.com</span></a> </span></b><span
                                                                style="font-family:&quot;Segoe UI&quot;,sans-serif,serif,EmojiFont;margin:0px;color:black"></span>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <b><span
                                                                    style="font-size:9pt;font-family:Candara,sans-serif,serif,EmojiFont;margin:0px;color:rgb(243,144,29);background-color:white">Siege : 128, rue de la Boétie - 75008 Paris</span></b><span
                                                                style="font-family:&quot;Segoe UI&quot;,sans-serif,serif,EmojiFont;margin:0px;color:black"></span>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <b><span
                                                                    style="font-size:9pt;font-family:Candara,sans-serif,serif,EmojiFont;margin:0px;color:rgb(243,144,29);background-color:white">Agence Paris : Tour Montparnasse - 33 rue du Maine - 75 015 Paris</span></b><span
                                                                style="font-family:&quot;Segoe UI&quot;,sans-serif,serif,EmojiFont;margin:0px;color:black"></span>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <span style="font-family:&quot;Segoe UI&quot;,sans-serif,serif,EmojiFont;margin:0px;color:black"> </span>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <i><span
                                                                    style="font-size:9pt;font-family:Arial,sans-serif,serif,EmojiFont;margin:0px;color:green">Pensez à l’environnement. N’imprimez cet email que si vous en avez vraiment besoin.</span></i><span
                                                                style="font-family:&quot;Segoe UI&quot;,sans-serif,serif,EmojiFont;margin:0px;color:black"></span>
                                                        </p>
                                                        <p style="color:rgb(36,36,36);text-align:start;background-color:rgb(255,255,255);font-size:12pt;font-family:Calibri,sans-serif;margin:0px">
                                                            <i><span
                                                                    style="font-size:9pt;font-family:Arial,sans-serif,serif,EmojiFont;margin:0px;color:green">Si vous l&#39;imprimez, n’oubliez pas de le recycler.</span></i>
                                                        </p>
                                                        <br>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <br>
                </div>
            </div>

        </div>
    </blockquote>
</div><br clear="all">
<div><br></div>-- <br>
<div dir="ltr">
    <div dir="ltr">EL HASSANE</div>
</div>
"""
# xx = parse_email_content_html(karim)
# print(xx)
