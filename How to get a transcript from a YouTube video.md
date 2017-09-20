Original instructions taken from here:
https://nathanwailes.atlassian.net/wiki/spaces/MTOVT/pages/1409098/Writing

1.  Get the HTML containing the transcript into Notepad++.  
    1.  Background
        1.  We are doing this so that we can extract the transcript from its surrounding HTML.
        1.  Sublime Text 2 can work as well, but it takes a long time to manipulate large transcripts from long videos (1.5 hours or more), whereas Notepad++ has no such problem.
    1.  Step-by-step process
        1.  Using Chrome, navigate to the video's URL, click the "More" button, and select the 'Transcript" option.
        1.  A div will become visible underneath the "More" button that will say "Transcript" and will have a closed drop-down box that says something like "English (Automatic Captions)".
        1.  Click the drop-down box and click the option that says "English (Automatic Captions)".
            1.  There will usually only be one option in the drop-down box.
        1.  The transcript should then become visible underneath the drop-down box.
        1.  Right click one of the lines in the transcript and select "Inspect".
        1.  When Chrome's Devtools open up, select the parent div of the one-line-of-the-transcript.
            1.  As I'm writing this, the id of the parent div is "transcript-scrollbox".
        1.  Right click that div and select "Edit as HTML".
        1.  The unmodifiable HTML source code should change into a modifiable text-box containing the same source code.
        1.  Click into the text-box and press "Ctrl + a" to select all of the HTML in that div.
        1.  Press "Ctrl + c" to copy the source.
        1.  Open up Notepad++ and, if necessary, create a new document.
        1.  Paste in the source HTML that you just copied.
1.  Hit "Ctrl + h" to open the "Replace" search box.
1.  Make sure that the "Search Mode" in the "Replace" box is set to "Regular expression".
1.  Get rid of the HTML tags and timestamps (eg _"1:18:29"_).
    1.  For "Find what", put `<.*?>|(?:[\d:]*\d:[\d:]+)`
    1.  For "Replace with", put a single empty space: " " (without the quotation marks).
    1.  Click "Replace all".
1.  Get rid of the excess spaces that were created when removing the HTML tags / timestamps.
    1.  In the "Find what" box, put `\s\s+`
    1.  In the "Replace with" box, leave it as a single empty space.
    1.  Click "Replace all".
1.  The document should now be all and only the transcription of the video.
