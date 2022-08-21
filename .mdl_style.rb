# Style file for markdownlint

all

exclude_rule 'fenced-code-language' # Fenced code blocks should have a language specified
exclude_rule 'no-inline-html' # This rule is triggered whenever raw HTML is used in a markdown document:

#Excluded to work with mkdocs material
exclude_rule 'MD046'
exclude_rule 'MD009'
exclude_rule 'MD026'

# Line lenght
rule 'MD013', :line_length => 120, :code_blocks => false, :tables => false

# Unordered list indentation
rule 'MD007', :indent => 2

# Ordered list item prefix
rule 'MD029', :style => 'ordered'
