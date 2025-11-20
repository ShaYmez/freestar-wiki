# GitHub Pages Setup Instructions

After merging this PR, you'll need to enable GitHub Pages in the repository settings:

## Steps to Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/FreeSTAR-Network/freestar-everywhere-wiki`

2. Click on **Settings** (gear icon)

3. In the left sidebar, click on **Pages** (under "Code and automation")

4. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
   
5. Save the settings

## First Deployment

After enabling GitHub Pages:

1. The workflow will automatically run on the next push to the `main` branch
2. Alternatively, you can manually trigger it:
   - Go to the **Actions** tab
   - Select "Deploy MkDocs to GitHub Pages"
   - Click **Run workflow**
   - Select the `main` branch
   - Click the green **Run workflow** button

## Accessing Your Site

Once deployed, your wiki will be available at:
- **Project Site**: `https://freestar-network.github.io/freestar-everywhere-wiki/`

The exact URL will be shown in the GitHub Pages settings after the first successful deployment.

## Troubleshooting

If the deployment fails:
1. Check the Actions tab for error logs
2. Ensure the workflow has the necessary permissions (Settings > Actions > General > Workflow permissions)
3. Verify that GitHub Pages is enabled with "GitHub Actions" as the source
4. Make sure the `main` branch exists and has the workflow file

## Notes

- The site will automatically rebuild and redeploy whenever changes are pushed to the `main` branch
- Build time is typically 1-2 minutes
- The site may take a few minutes to update after deployment completes
