This skill is for creating Mermaid images.

Node.js and pnpm must be installed first.

pnpm add -g @mermaid-js/mermaid-cli
mmdc --version

Example diagram file: `diagram.mmd`

"""mermaid
flowchart TD
    A[Idea] --> B[AI Agent]
    B --> C[Design]
    C --> D[Code]
    D --> E[Test]
    E --> F[Deploy]
"""

Generate SVG:
mmdc -i diagram.mmd -o diagram.svg
