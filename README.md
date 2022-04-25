# Team-Cymru-Download-Logs
Team Cymru provides daily lists of compromised or abused devices for the ASNs and/or netblocks with a CSIRT’s jurisdiction. This includes such information as bot infected hosts, command and control systems, open resolvers, malware urls, phishing urls, and brute force attacks


# Other Options Enrichment with IntelMQ

<img width="545" alt="image" src="https://user-images.githubusercontent.com/87453279/165119672-e879456a-1a9e-44e4-9069-05e4451739e6.png">


### Team Cymru

### - Revision: 2018-01-20

### - Documentation: https://www.team-cymru.com/CSIRT-AP.html https://www.cymru.com/$certname/report_info.txt

### - Additional Information: “Two feeds types are offered:

  * The new https://www.cymru.com/$certname/$certname_{time[%Y%m%d]}.txt

  * and the old https://www.cymru.com/$certname/infected_{time[%Y%m%d]}.txt

Both formats are supported by the parser and the new one is recommended. As of 2019-09-12 the old format will be retired soon.”

### - Collector

### - Module: intelmq.bots.collectors.http.collector_http

### - Configuration Parameters:
   * http_password: {{your password}}

   * http_url: https://www.cymru.com/$certname/$certname_{time[%Y%m%d]}.txt

   * http_url_formatting: True

   * http_username: {{your login}}

   * name: CAP

   * provider: Team Cymru

   * rate_limit: 86400

### Parser

### - Module: intelmq.bots.parsers.cymru.parser_cap_program

### - Configuration Parameters:
