class HtmlOutputer(object):
    
    def __init__(self):
        self.datas=[]
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        
    def output_html(self):
        fout=open('out.html','w')
        fout.write("<meta http-equiv='Content-Type' content='text/html'; charset=>")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td><a href='%s'>%s</a></td>" % (data['url'],data['url']))
            fout.write("</tr>")
                
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
        
    



