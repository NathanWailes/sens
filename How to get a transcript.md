Original link:
https://nathanwailes.atlassian.net/wiki/spaces/MTOVT/pages/1409098/Writing

1.  Spend some time thinking up a basic outline of the points you would like to make.
    1.  This will help prevent you from creating an overly-long, rambling, poorly-organized video, which will be much harder to turn into easily-digestible prose.
2.  Record a video in which you go through the points you've decided you want to make.
    1.  Give examples and explanations where you feel they will help the listener / reader.  

        1.  This transcription method is especially good and helping you to quickly convey explanations and examples that would normally take a long time to type out.
    2.  Try to record in a quiet environment.
    3.  Try to speak clearly.
    4.  Try to speak at a distance from the microphone where your voice will be clear on the recording.
3.  Upload the video to YouTube.
4.  Wait for YouTube to create a transcription for your video.
    1.  This may be immediate; I'm not sure.
5.  Get the HTML containing the transcript into Notepad++.  

    1.  Background
        1.  We are doing this so that we can extract the transcript from its surrounding HTML.
        2.  Sublime Text 2 can work as well, but it takes a long time to manipulate large transcripts from long videos (1.5 hours or more), whereas Notepad++ has no such problem.
    2.  Step-by-step process
        1.  Using Chrome, navigate to the video's URL, click the "More" button, and select the 'Transcript" option.
        2.  A div will become visible underneath the "More" button that will say "Transcript" and will have a closed drop-down box that says something like "English (Automatic Captions)".
        3.  Click the drop-down box and click the option that says "English (Automatic Captions)".
            1.  There will usually only be one option in the drop-down box.
        4.  The transcript should then become visible underneath the drop-down box.
        5.  Right click one of the lines in the transcript and select "Inspect".
        6.  When Chrome's Devtools open up, select the parent div of the one-line-of-the-transcript.
            1.  As I'm writing this, the id of the parent div is "transcript-scrollbox".
        7.  Right click that div and select "Edit as HTML".
        8.  The unmodifiable HTML source code should change into a modifiable text-box containing the same source code.
        9.  Click into the text-box and press "Ctrl + a" to select all of the HTML in that div.
        10.  Press "Ctrl + c" to copy the source.
        11.  Open up Notepad++ and, if necessary, create a new document.
        12.  Paste in the source HTML that you just copied.
6.  Hit "Ctrl + h" to open the "Replace" search box.
7.  Make sure that the "Search Mode" in the "Replace" box is set to "Regular expression".
8.  Get rid of the HTML tags and timestamps (eg _"1:18:29"_).
    1.  For "Find what", put `<.*?>|(?:[\d:]*\d:[\d:]+)`
    2.  For "Replace with", put a single empty space: " " (without the quotation marks).
    3.  Click "Replace all".
9.  Get rid of the excess spaces that were created when removing the HTML tags / timestamps.
    1.  In the "Find what" box, put `\s\s+`
    2.  In the "Replace with" box, leave it as a single empty space.
    3.  Click "Replace all".
10.  The document should now be all and only the transcription of your speech.
