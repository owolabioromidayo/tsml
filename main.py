def l_gen(l):

def render_template(filename, _map):
    #parse
    transformed = []
    namespace = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
               
            #variable replacement
               for match in re.findall('\{\{[^0-9][a-zA-Z0-9 _]+\}\}', line):
                   key = match.replace('{','').replace('}','').strip()
                   if key in _map.keys():
                       line = line.replace(match, _map[key])
                       
            #handle for loops
                match  = re.findall('\{\%[^`0-9][a-zA-Z0-9 _]+\%\}', line)
                if match:
                    m = match[0]
                    expr = m.replace('{','').replace('}','').strip()
                    tokens = expr.split(' ')
                    if tokens > 4:
                            print('INvalid expr')
                    else:
                        new_var = tokens[1]
                        if tokens[-1] in _map.keys():
                            requested_var = _map[tokens[-1]]
                            namespace[new_var] = 
                        else:
                            print('Invalid Expr')

                    
            transformed.append(line)

def main():
    render_template('index.html',{s:'s'})
