import pypandoc

# Convert markdown to HTML with CSS
pypandoc.convert_file('resume.md', 'html', outputfile='resume.html', extra_args=['-c', 'resume-css-stylesheet.css'])

# Convert HTML to PDF
pypandoc.convert_file('resume.html', 'pdf', outputfile='resume.pdf', extra_args=['-t', 'html5'])

# Convert markdown to DOC with reference document
pypandoc.convert_file('resume.md', 'docx', outputfile='resume.doc', extra_args=['--reference-docx=resume-docx-reference.docx'])

