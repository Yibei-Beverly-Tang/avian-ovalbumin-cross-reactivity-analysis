# Upload to GitHub

## Create the repository

1. Open <https://github.com/new>.
2. Repository name: `avian-ovalbumin-cross-reactivity-analysis`.
3. Choose `Public` or `Private`.
4. Do not add a README, `.gitignore`, or license on GitHub; they are already in
   this project.
5. Select **Create repository**.

## Upload with the GitHub website

1. Extract the supplied project ZIP on your computer.
2. On the empty repository page, select **uploading an existing file**.
3. Drag all extracted files and folders into the upload area. Upload the
   extracted contents, not the ZIP file itself.
4. Commit summary:

   `Initialize evidence-traceable avian ovalbumin project v0.1.0`

5. Select **Commit directly to the main branch**, then choose
   **Commit changes**.

Hidden files such as `.gitignore` and the `.github` workflow directory should
also be included. The local `.git` directory is intentionally not included in
the upload package.

## Upload a later full-project update

After extracting the newer project ZIP, upload all extracted contents to the
existing repository. GitHub will identify modified and new files. For the
v0.2.0 sequence-catalogue update, use this commit summary:

`Add verified avian ovalbumin sequence catalogue v0.2.0`
