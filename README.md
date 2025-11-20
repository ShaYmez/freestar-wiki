# FreeSTAR Everywhere Wiki

This repository contains the documentation for the FreeSTAR Everywhere project, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the development server:
   ```bash
   mkdocs serve
   ```

3. Open your browser and navigate to `http://localhost:8000`

### Building the Site

To build the static site:

```bash
mkdocs build
```

The built site will be available in the `site/` directory.

## 📦 Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

The deployment is handled by the GitHub Actions workflow defined in `.github/workflows/deploy.yml`.

### Manual Deployment

You can manually trigger a deployment by:
1. Going to the Actions tab in GitHub
2. Selecting the "Deploy MkDocs to GitHub Pages" workflow
3. Clicking "Run workflow"

## 📁 Repository Structure

```
.
├── docs/               # Documentation source files
│   ├── index.md       # Home page
│   ├── getting-started.md
│   └── about.md
├── .github/
│   └── workflows/
│       └── deploy.yml # GitHub Actions workflow
├── mkdocs.yml         # MkDocs configuration
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## 🛠️ Configuration

The site configuration is defined in `mkdocs.yml`. Key settings include:

- **Site name**: FreeSTAR Everywhere Wiki
- **Theme**: Material for MkDocs
- **Color scheme**: Blue primary, Orange accent

## 📝 Adding Content

1. Create or edit Markdown files in the `docs/` directory
2. Update the navigation in `mkdocs.yml` if needed
3. Commit and push your changes
4. The site will automatically rebuild and deploy

## 🔗 Links

- [GitHub Repository](https://github.com/FreeSTAR-Network/freestar-everywhere-wiki)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

## 📄 License

This documentation is part of the FreeSTAR Everywhere project.
