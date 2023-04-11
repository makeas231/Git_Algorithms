def line_alignment(list_: list[str], k: int) -> list[str]:
    lines = []
    current_line = []
    current_length = 0
    
    for word in list_:
        if current_length + len(word) + len(current_line) <= k:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(current_line)

    aligned_lines = []
    for line in lines:
        num_spaces = k - sum(len(word) for word in line)
        num_gaps = len(line) - 1
        if num_gaps == 0:
            aligned_lines.append(line[0] + ' ' * num_spaces)
        else:
            spaces_per_gap = num_spaces // num_gaps
            extra_spaces = num_spaces % num_gaps
        
            aligned_line = ''
            for i in range(len(line)):
                aligned_line += line[i]
                if i < len(line) - 1:
                    aligned_line += ' ' * spaces_per_gap
                    if i < extra_spaces:
                        aligned_line += ' '
            
            aligned_lines.append(aligned_line)
    
    return aligned_lines


