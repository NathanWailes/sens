# Background
- The idea here is to gather [Aubrey's answers to Quora questions](https://www.quora.com/profile/Aubrey-de-Grey) so that they can be searched more easily.
- Note that the goal is to *only* have those of his answers that are relevant to SENS. Aubrey also talks about mathematics on Quora, and that generally won't be of interest to us.
- Newer questions at the top.
  - It isn't clear to me whether it's better to have them at the bottom or the top.
- It would be nice to have a Python script that would scrape these automatically and store them at some easily-accessible URL...
- The script would ideally get not only the answers, but also Aubrey's responses to comments.

# TODO
- I have gathered all of the basic text of his answers until 2017.10.11.
- I gave up on getting the dates, so that's something else to gather.
- I also didn't gave up on gathering the comments, so that's another thing to do.

# Questions

##### How can I apply to SENS for funding?
2017.10.08 - http://www.sens.org/research/grant-submission-process

##### What is the significance of the failure of monoclonal antibodies that remove amyloid beta as an attempt to slow the progression of Alzheimer's disease to longevity research?
2017.09.25 - Less than most commentators say. Abeta may or may not be causative in AD, and if it is there are many ways in which it could be, but the important thing to remember is that AD is complicated, which means that the repair of more than one of its features may deliver more than the sum of the benefits arising from repairing each one in isolation. We have Abeta removal in our back pocket now as a tool that can be combined with other tools (such as tau removal) as and when the latter are developed. Whether it’s needed remains to be seen, but I’m very happy that we now have the option.

##### Why are billionaires that support the SENS agenda not really funding it?
2017.09.25 - Yeah… well, the thing about not funding someone is you don’t tend to be all that forthcoming about why you decided no… but my best inference is that there is no one answer, every HNWI is different. Sometimes they don’t think non-profits work. Sometimes they are scared that the approach is still unproven so they want to wait and see. Sometimes their spouse is virulently opposed. Sometimes they think other causes are more important. Sometimes they have a bad vibe about me personally. Sometimes they don’t like to do things that other HNWIs are not doing and they don’t consider Thiel to be a reliable first-mover. For each of the above reasons I could (but I won’t!) name at least one HNWI who I believe is substantially an example.

##### How much money does Aubrey de Grey need to find a cure?
2017.09.22 - Short answer: $1 billion over 10 years would do it with high probability.

Longer answer: clearly the question is not whether but when aging will be brought under comprehensive medical control. Thus, the right question is how much money is needed, over what time period, to hasten that time to the point where money will not make much difference any more because the rate of progress is limited by the simple difficulty of the research. See above for the number!

Key other number: at current funding levels we are going so slowly that (by my current estimate) we could easily end up delaying the defeat of aging by a decade. Therefore, even low-balling the expectations, every $2 spent in supporting this work would save a life. That compares very favourably with anything else.

##### What's been the progress, if any, on the WILT (Whole-body interdiction of the lengthening of telomeres) strategy?
2017.07.23 - It’s been slow but steady. On the telomere control side, other groups have made nice progress in inhibiting telomerase-mediated elongation (see especially Jerry Shay’s 2015 paper on 6-thio-2′-deoxyguanosine) and we have developed a much faster and cheaper assay for ALT that will facilitate the discovery of anti-ALT drugs. On the stem cell replacement side, we funded a study to look for the ability of early-generation telomerase-knockout haematopoietic stem cells to rescue longevity in late-generation telomerase knockout mice, and it worked (it was tricky because we needed to rescue their gut problems with another mutation) but we could only afford to do a small study so we barely made it to statistical significance and we haven’t published it. Our parallel work on the gut, led by Graca Almeida-Porada at Wake Forest, made modest progress but unfortunately we have had to suspend that project because of lack of funds.

I remain hopeful that we can get WILT to work - but I also remain hopeful that we won’t need to, because simpler therapies will work well enough. In particular, the progress in cancer immunotherapy over recent years has been dramatic, and it might just be enough to make WILT unnecessary. We won’t stop working on WILT until we’re sure that that is the case, though!

##### Do induced pluripotent stem cells reverse the intracellular junk that accumulates with aging?
2017.05.25 - Sure they do, but not because they are pluripotent: simply because the divide. Cell division shares out any junk between the daughter cells, so it dilutes it away.

##### Aubrey de Grey, what do you mean by "longevity escape velocity"?
2017.05.26 - The thing you’re overlooking is that the “first-generation” panel of rejuvenation therapies will not be perfect: it will mostly plug the gaps that evolution has left in our in-built damage-repair machinery, but it won’t do so 100%. (Let’s just define the damage that it does repair as the easy damage and the rest as the difficult damage.) There is nothing to stop us from applying those therapies every year, never mind every 30 years - but because of their incompleteness, however often we apply them we will still get back to biologically the same age (i.e., we’ll be carrying the same quantity of damage) at some point (I generally guess chronological age 90, but that’s a total guess) as we were just before we first applied the therapies. And the problem is, that the overwhelming majority of the damage that is present at that point will be difficult damage.

Thus, the only way we will be able to re-rejuvenate these people is if we have improved the therapies. And of course this carries on being true until such time as the therapies become truly 100% comprehensive, which quite probably will never happen. Hence the need to keep pushing ever closer towards that probably-unachievable goal. LEV is simple the minimum pace at which we need to do that, in order to keep one step ahead of the problem.

The good news is that LEV slows down as time passes, because the smaller the remaining gaps in the therapies, the longer it takes for that still-too-difficult damage to become abundant enough to make us sick.

##### Could CRISPR-modified CAR-T-cells clear senescent cells?
2017.03.27 - I’m guessing the question is stimulated by this recent study:

http://www.nature.com/nature/journal/v543/n7643/full/nature21405.html

Short answer: maybe, but it won’t be the end of the world if not, because there are now quite a few promising-looking ways to clear them. Our latest focus in this area is somewhat related: we’re starting to look at improving clearance with another arm of the immune system, NK cells, which are already known to clear most senescent cells following would healing so may be easiest to augment to do that job more thoroughly.

##### What does Aubrey de Grey think about the potential reversal of ageing in humans through Dr. Keizer's modified FOXO4-p53 interfering peptide?
2017.03.25 - The result is important, and the “DRI” technology used to do it is potentially even more important because it is so broadly applicable. We’ve known for a while that the elimination of senescent cells is a major plank of rejuvenation, and this is a further confirmation, with the advantage that it is underpinned by good scientific understanding of the mechanism.

##### What drugs can enhance the autophagy function of cells?
2017.03.14 - It’s important to remember that “autophagy” refers, strictly, to the processes that transport waste products to the lysosome, and not to the destruction of that waste once it gets there. This is not semantic hair-splitting, because it’s seductive but counterproductive to assume that enhancing autophagy will sustainably reduce the abundance of undigested waste in the rest of the cell. If there is too much such waste and the root cause of that is the lysosome’s inability to destroy it, no amount of enhancement of autophagy will help. And unfortunately, impairment (such as in aging) of lysosomal catabolic function seems to result, mainly, from the fact that that function is never 100% comprehensive even in youth, hence some types of waste accumulate there throughout life, with eventual upstream “traffic jam” consequences.

So there are plenty of answers to the question as asked, but really it’s the wrong question. The better question is, what drugs can sustainably enhance the lysosomal elimination of waste? And the answer to that, at present, is “none”. Enhancing that elimination requires enhancing the lysosome itself, which can only be done by giving it additional enzymes so that it can destroy stuff that it normally can’t. We’ve made good progress on that in a couple of key areas, atherosclerosis (oxidised cholesterol) and macular degeneration (derivatives of vitamin A), and both those programs have now been spun out into startups (Human Regenerative Biotechnologies and Ichor Therapeutics). We’ve recently started a new program in this area, targeting neurofibrillary tangles in Alzheimer’s.

##### Will Aubrey de Grey do a talk in France (or has he done one)?
I’ve given quite a few talks in France over the years. I haven’t honestly noticed a particularly greater susceptibility to this sort of thinking than elsewhere.

##### Which advice would Aubrey de Grey give to somebody with lupus erythematosus or arthritis as an autoimmune disease?
I’d advise consulting a medical professional, rather than anyone like myself whose doctorate is a PhD. We’re working on rejuvenating the immune system, which will certainly address autoimmunity to some extent as well as regular immune dysfunction, but our work on this, as on everything, is early-stage research and is years from being ready for prime time.

##### What does Aubrey de Grey think about the longevity pill Niagen?
Aubrey:
> Tim has it right.

Tim Amann:
> I obviously can’t speak for Aubrey de Grey, but I suspect he wouldn’t be interested in, or advocate for, Niagen. Niagen is a calorie restriction (CR) mimetic - a substance that supposedly mimics the effects of CR, which has been shown to have a significant longevity effect on short-lived organisms, but far less so on longer-lived organisms. Summing up the many things he has said about CR in the past, I would say he thinks CR would have little effect on human longevity. I wouldn’t say that he is against it. It’s just not his focus and not a game-changer in relation to aging.
> 
> In short, de Grey’s strategies are centered around removing and repairing the seven major forms of damage caused by aging (analogous to maintaining a classic car). He’s not attempting to stop or reverse the aging process (meaning he’s not trying to stop the damage from aging from occurring), which he would say is not doable for a very very long time due to the complexity of human metabolism.
> 
> CR mimetics are based on the idea of slowing the aging process (Niagen, Resveratrol, Metformin - pretty much any current “anti-aging pill”), but again, these will likely have little effect on longer-lived species like humans. Metformin will be going through a clinical trial, so we’ll know more soon, but I wouldn’t expect anything dramatic in relation to lifespan. I think de Grey estimated CR can provide, at the most, 2 to 3 more years in humans.
> 
> Niagen could potentially provide some benefits from a healthspan perspective (increased energy, potentially), but evidence is lacking. Time will tell.

##### Is it true that thanks to our technologies on aging, we have exceeded the limit of “in a lived year, we have gained more than a year to live”?
Definitely not. The rate at which the headline life expectancy numbers rise, which is a couple of months per year, does understate the situation for any given individual (basically because the headline numbers are statistical constructs generated from people born in different years), but it definitely doesn’t understate it enough to mean that we are already at “longevity escape velocity”. However, I remain of the view that we have at least a 50% chance of getting to that point within the next 20 years.

##### Is the first 5 year old mouse already alive (and is ongoing an anti-aging trial)?
Probably not - the current record of just one week shy of five years probably can’t be beaten by any practicable genetic manipulation. But what matters much more is what can be achieved using only interventions performed when the mouse is already alive, and ideally already middle-aged. At present the record for that is less than four years, so reaching five years is a very tall order - but I think there’s a good chance that the first such mouse will be born within five years.

##### Are there any good ways to invest in anti-aging research/therapies?
Wow… I’m not sure where to start with this one. The number of ways to invest in this space is exploding, and the most basic Google search will lead you to a host of opportunities. If you want more sophisticated advice on the best investment options. write to me at aubrey@sens.org and I’ll be happy to help.

##### How do T-lymphocytes have a lifespan that is infinite (according to my teacher)? Don't the telomeres get shorter until the cell dies?
T cells (and also B cells) turn on telomerase when they are in the highly proliferative phase, so they compensate for the telomere shortening that you’re thinking of. However, this telomerase activation weakens in old age, and that’s generally thought to be a big contributor to the age-related decline in the power of the immune system.

##### What's Aubrey de Grey's position on telomerase activators?
I’m very much on the fence. The question of whether telomerase activation will have decisive long-term negative consequences in terms of cancer is one that we cannot currently answer with confidence. Therefore, I very much endorse and support the research and clinical trials currently underway on telomerase activation, while at the same time SENS Research Foundation itself is heavily engaged in research to do the opposite, suppressing telomere elongation as an anti-cancer strategy.

##### Can we increase our maximum lifespan just by clearing senescent cells, beta amyloids, transthyretin and by immune system rejuvenation? Can we reach 150 years old?
What George said. The body accumulates many types of damage in the course of its normal operation, any of which will kill us on schedule unless it is eliminated (i.e., repaired) before it reaches fatal levels,however well we fix all the others. Fixing one major type of damage will **somewhat** slow down the accumultion of others, and I’ll admit that the magnitude of this interdependence may be a fair bit more than I would have thought before the results of the past few years in the senescent cell elimination area, but still, adding 70 years to today’s average lifespan of 80 is highly unlikely until we can rather thoroughly repair all seven of the main categories of damage.

##### What is your review of SENS Foundation?
Check out our annual report which should be released around the end of January.

##### What are the best indications of progress in anti-aging technologies we can expect by the end of 2021?
Clinical trials of most (though probably not all) of the key damage-repair interventions that SENS Research Foundation pursues. See here:

[Project|21 Announcement](http://www.sens.org/outreach/press-releases/project21-announcement)

###### Comments
- Randall Burns: You had said in a previous posts you thought longevity studies on effects of adult HGH supplementation on mice who either lack growth hormone or lack the known growth hormone receptor might be a good idea. Do you think we may see studies in that area any time soon?
  - Aubrey: It’s a rather obvious experiment and not very difficult except insofar as any lifespan experiment is expensive, so I’m surprised that it still hasn’t been done. If I had the money I’d commission it!
  - Randall Burns: Do you know anyone who could give the approiximate budget needed?
  - Aubrey: Probably $20k minimum…

##### What is Aubrey De Grey's response to the skepticism of some scientists such as PZ Myers?
The personal answer is that generally I don’t waste my time on people who are more interested in attracting readership by writing derogatory and pathetically uninformed drivel than in contacting me for actual facts.

The more important answer is that careless professional skeptics do a lot of harm by seducing the public into believing their uninformed skepticism and thereby sapping funding for life-saving research. I wrote about this in my most recent editorial for Rejuvenation Research, in reaction to a piece in Scientific American by Michael Shermer that uncannily resembles the Myers one.

##### Does the fact that different negligibly senescent species have different lifespans prove that aging is not caused by damage but by a genetic program?
By definition, any difference in lifespan between two negligibly-senescent species is caused by differences in extrinsic causes of death, not by aging.

The difference in rate of aging between species that DO age is certainly determined by genetics, but not in the way that you seem to be thinking. It is determined by the degree of comprehensiveness of the arsenal of genetically-encoded machinery that repairs damage as that damage is generated. There is not, by contrast, any program that actively creates such damage (or inhibits that anti-aging machinery) on purpose. See the paper I wrote on this topic last year.

##### If people with Laron Syndrome do not exhibit any lifespan extension, can we extrapolate the same to calorie restriction in humans?
Calorie restriction works less well in longer-lived species, because long famines are rarer than short ones so the selective pressure to maintain the genetic machinery to adapt to them is less. See my paper in Gerontology from 2005. The same applies to any genetic or pharmacological emulation of CR, since by definition they work through the same pathways as CR itself does.

##### What does Aubrey de Grey think of the possible appointment of Jim O'Neill as the head of the FDA?
I think he would be a huge asset. He combines two vital qualities: the vision to see what needs to be done in such an influential role, and the diplomacy to carve through the thicket of vested interests that so often impedes necessary change. I hope he gets the job.

##### What does Aubrey de Grey (or other leading longevity researchers) think about cord blood banking?
My view is that it is a useful thing to do, but not for anti-aging purposes, because the progress we make in (ten, let alone) 50 years in medical research massively exceeds the difference in difficulty between doing things with young cells versus old cells. I have made the same argument in relation to germ line gene therapy.

##### Of all the startups funded by Breakout Labs, which are Aubrey de Grey's favorites?
Hard to say, actually, because they’ve funded quite a few really amazing companies - some of them on my introduction. Among the very first crop, I must mention Arigos, Immusoft and 3scan, all of which are focused on sensational technologies.

##### How does Alagebrium work in breaking crosslinks up?
The most recent work on this is the following study from the lab of David Spiegel, whom we fund to work on glycation-induced crosslinks:

[The unique reactivity of N-phenacyl-derived thiazolium salts toward α-dicarbonyl compounds.](https://www.ncbi.nlm.nih.gov/pubmed/23186164)

##### What does SENS foundation think of a gene network stability model of ageing and the medical research strategies resulting from it?
It's a nice study (and I know Fedichev quite well). But the problem with all studies of this kind is that it isn't informative to demonstrate that one's model reproduces the pattern of aging and lifespan that is seen in nature, because it turns out that lots of models do that, including extremely different models. And one can't really say that there's a case for a treatment that is inspired by a particular model but not by another that reproduces real-world aging equally well.

##### If cancer cells are immortal, how do they solve the problem of error accumulation of DNAs and proteins?
Proteins are no problem because any garbage is diluted out every time a cell divides. DNA errors are a big problem for most cells of a cancer, but for the cancer overall they are vital, as they are the source of the genetic diversity that lets the cancer outwit the immune system etc.

##### How many different forms of intra- and extracellular 'gunk' will need to be cleaned up for the SENS anti-aging approach to work?
Great question. We don't really know, of course. At present our focus is on just three of each (intra and extra), but transthyretin's role in the extreme elderly has only been known for a few years, and I would be quite surprised if new examples don't turn up pretty soon. The good news, though, is of course that the same methodology should lead to the therapies for each case, such that we can take advantage of what we learned for the first examples to speed up the pipeline for later ones. So actually, and especially when we factor in the longevity escape velocity dimension, the viability and timetable of the SENS strategy doesn't depend too badly on how many such compounds will need to be cleaned up.

##### What's Aubrey de Grey worth, and where did he get the money to personally support SENS research?
As of now my net worth is around $2M, of which only a small minority is in any way disposable. I inherited about $16.5M from my mother in 2001, of which I donated about $13M to SENS Research Foundation (or more precisely to our UK affiliate). Of the remainder, on which inheritance tax was payable so it was reduced to about $2M, I spent the majority on the house where I now live, in the Santa Cruz mountains.

So far so good - but I will take this opportunity to mention that I and my colleagues at SENS decided in 2011 to spend this money over a period of five years, which we judged to be a good balance between getting it put to good research use and keeping us afloat long enough to bring in additional money. The research has gone great, but the fundraising is still mighty dicey. All help gratefully received!

##### Do aging of stemcells determine the longevity of an organism alone since short lives of normal body cells do not affect the organism's longevity?
No, for several reasons. The main reasons are:

- there is aging of material outside the cell, such as crosslinking of the extracellular matrix that causes loss of elasticity, leading to things like hypertension
- many cells just hang out for life, neither dividing nor being replaced, and they age internally
- cells can get damaged and refuse to die when they should, or to stay quiescent when they should

##### Why is Aubrey de Grey so optimistic about his predictions, considering no SENS therapy has been shown to extend lifespan yet?
The lack of such data is irrelevant to the assessment of whether SENS is likely to work on the kind of timeframes I’ve predicted. The idea that it would be relevant is akin to the idea that cars can’t work because no individual component of a car exhibits motion when burning gasoline is poured on it. Medicine is a branch of engineering, and engineering doesn’t work additively. Putting it in more biological terms: each type of damage in the body is protected against by a different set of genes (though the sets overlap), so evolution will gravitate to a quality of those genes that results in the respective types of damage all becoming life-threatening at about the same age. Thus, fixing any one such type of damage (or even most of them) will not appreciably postpone the ill-health of old age.

##### What does Aubrey de Grey think about the way Michael Fossel and Bill Andrews are trying to tackle aging?
Short answer: yes but not yet, and the much-discussed diversity of expert opinion on this topic actually entirely misses the point.

Long answer: it’d definitely be very valuable if we had a way to really really totally control cancer that did not involve preventing telomere elongation, which we may indeed have within not too long if the recent progress in cancer immunotherapy continues, but we may not. If we don’t achieve such control, it may well be that the only way we can develop to control cancer really thoroughly is by very robustly preventing telomere elongation, which will inevitably result in the creation of problems in rapidly-renewing tissues (such as the gut and the blood) even if those problems don’t currently exist (which is the focus of expert debate that I mentioned above). We’re working on doing exactly that in combination with stem cell therapies to alleviate any such side-effects. But for now, I’d say one should be cautious, because we can’t yet even tell reliably whether someone has early-stage cancer, let alone cure it.

##### Would someone who is 80 benefit from SENS therapies or is it too old to rejuvenate them?
Depends on their state of health. Best way to think about this is in terms of how many more years the person can be expected to live, rather than how long ago they were born. The bad news is that the things we can control as regards how much longer we can live are much less influential than the things we can’t control, such as our genetics.

##### At the exponential rate at which longevity movements are advancing, can radical life extension be achieved gradually over the next decade?
No, I don’t think it will be gradual. I believe that life expectancy will actually level off for the next decade or two before damage repair therapies arrive, and that when they do it will skyrocket. There will be a rather sharp cusp.

##### Which, if any, of the existing alleged anti-aging supplements does someone like Aubrey de Grey believe in and use personally?
I don’t personally take anything, but that should not be interpreted as advice to others not to. My way of looking at this is to start from three very basic principles:

1. Nothing simple, which means nothing we have today, can possibly benefit most people dramatically, only very slightly. That’s because both the body and its aging are really complicated, and one can’t dramatically alter the behaviour of a really complex system by simple means, other than if the system already has inbuilt machinery to respond to that simple stimulus. There is one example of such machinery, namely the response to famine, but for obvious evolutionary reasons (basically just that long famines are rarer than short ones) the response to famine in long-lived species like humans is much milder than in short-lived ones.
2. Everyone’s metabolism is different, so the only way to really tell what works for you is to listen to your body, not to trust books.
3. I’ve been tested very thoroughly several times over the past 15 years and I always come out with a very young biological age. Thus, for me the best policy is to be conservative in terms of doing anything new: if it ain’t broke don’t fix it.

##### When will aging be reclassified as a disease?
Aging (defined as the physiological decline that everyone currently experiences with advancing years after about 40) unquestionably causes astronomical amounts of suffering, in the modern world adding up to more than all other human experiences put together. Thus, it is exceptionally demoralizing to see educated people continuing to find such crass ways to put it out of their minds, like comparing it with left-handedness. Aging is unequivocally a medical condition that is potentially amenable to medical intervention, and as such it is vital that such interventions be developed as soon as possible and therefore that the quest to do so be supported, not trivialized.

Whether aging should be called a disease, however, is a question with additional ramifications. “Disease” - like “immortality” and “cure” - is a word that has an established meaning that has already been obfuscated to the detriment of progress: in particular, it has been extremely unfortunate that conditions such as Alzheimer’s are called diseases, because that gives the impression that they can be “cured” - eliminated from the body entirely, like an infection - when in fact they are parts of aging and as such are side-effects of being alive. I am OK with calling aging an “uber-disease” that encompasses all aspects of the ill-health of old age, but no more. But the thing that really matters is not whether we call aging a disease but whether we call it a condition for which treatments can be approved and reimbursed. That, I’m overjoyed to say, is a question on which there has recently been fantastic progress, spearheaded by Nir Barzilai and colleagues, in the form of the TAME trial for metformin. The definition of the endpoint, in terms of the presence of more than one of the key features of age-related ill-health, is a perfectly good practical definition of aging, and even if the TAME trial itself is unsuccessful, the precedent that it has laid down in terms of how to structure future clinical trials will stand and will be copied increasingly often. That makes me very happy.

##### Can we try all present day rejuvenation technologies combined on mice?
Sure. The problem is that any such experiment needs to be done on a rather large scale, so as to identify which components are working, are interacting synergistically, or are interacting antagonistically. But this is a key part of implementing SENS properly, so it must be done soon. We are unable to embark on it thus far at SENS Research Foundation due to lack of funds, but we’re trying our best to change that!

##### According to the paper doi: 10.1038/nature20578 does it mean that we completely stopped the aging processes in mice?
No, nothing of the kind. This is a suspension of embryonic development at a very early stage, and it has nothing to do with aging of an adult animal.

##### Can triphala\chebulic acid break glucosepane crosslinks? Can it increase lifespan?
I asked my colleague Michael Rae to look into this, and here is his answer:

There's certainly no good evidence that it does either. While chebulic acid is being promoted as an inhibitor and even breaker of advanced glycation endproducts (AGE), there are numerous deep limits and/or flaws in the research underlying this claim.

First, all of the research reporting inhibition or breakage of AGE by chebulic acid was conducted in Petri dishes, reacting pure isolated chebulic acid with artificially-generated so-called AGE molecules (I'll come back to that last point in a moment). It is always best to be skeptical of such "in vitro" studies, because the way that molecules behave in a living organism can often be quite different from the way it behaves in an isolated system. This is especially so for the two halves of the question here — AGE and glycation products on the one hand, and compounds like chebulic acid on the other. Chebulic acid is a phenolic acid, part of the family of compounds generally referred to as "polyphenols," and such compounds tend to be very heavily metabolized by enzymes in the gut microbiome, the intestine, and finally the liver before being absorbed (if they are absorbed at all) into the circulation.

I can find no studies that monitored the absorption and biotransformation of chebulic acid into metabolites, and indeed, the authors of several scientific papers on chebulic acid have highlighted lack of such studies as an important limitation to the physiological significance of their reported results using the compound. One study attempted to get a preliminary handle on this issue using a much less expensive simulation of digestion using a series of reactors with different conditions mimicking the conditions of different parts of the GI tract on chebulic acid and related molecules in Terminalia chebulia. The results of this study suggests that much of an oral dose of either compound will be degraded into simpler molecules in the upper GI tract, and that much of what reaches lower down will largely be metabolized by the gut bacteria into compounds called urolithins, which are degradation products of polyphenols that (on the one hand) tend to be better absorbed than the original compound, but which (on the other hand) tend to be metabolized into still other compounds that are less reactive than the original urothelin, and whose biological activity is unknown. So it seems unlikely that any intact, pure chebulic acid will even reach your tissues to exert the effects reported in the Petri dish studies, let alone at a concentration adequate to exert any meaningful biological effect.

Additionally, the formation and maturation of glycation products is dictated by the specifics of the complex physical and chemical environment of the body, including factors like temperature, the concentration of sugars, the structure of proteins, and the presence of transition metals and free radicals in body fluids. While the studies on chebulic acid in glycation chemistry have been carried out at body temperature, they have not attempted to simulate physiological conditions in other ways, making the results suspect.

Then there is the matter of what these in vitro studies are actually testing. The compounds that have been labeled AGE in recent studies are not clearly AGE at all, are even less likely to be AGE encountered in the body, and are fairly clearly not glucosepane. Some studies have used proteins from the lens of the eye and reacted them with threose, a degradation product of vitamin C that has been hypothesized to be involved in the crosslinking of such proteins because vitamin C itself is present in the human lens at about double the concentration of glucose. However, studies that have looked for the early products of threose reacting in proteins in the body on the way to forming AGE have failed to find any, either in the human lens or elsewhere, and there's no particular reason to think that such products would lead to the formation of glucosepane even if they did form.

Another study, which purported to show not only the inhibition of the formation of early glycation products but the actual breakage of mature AGE, generated the glycation products by reacting glycated circulating proteins with collagen, but did not actually test to see what product they had made;

[FEEDBACK FROM "GLYCOSENS PANEL" FITS IN HERE]

Overall, it seems unlikely that chebulic acid breaks /any/ AGE crosslink in the body, and even less likely that it can break glucosepane.

<Nathan Wailes TODO: Get the links below working.>

[21308613 24759763 20659546[uid] - PubMed - NCBI]

[In Vitro Bioaccessibility, Human Gut Microbiota Metabolites and Hepatoprotective Potential of Chebulic Ellagitannins: A Case of Padma Hepaten® Formulation](http://www.mdpi.com/2072-6643/7/10/5406/htm)

http://www.jbiopharm.com/

[World Journal of Otorhinolaryngology...](http://www.wjgnet.com/2218-6247/)

Statistical optimization of process parameters influencing the biotransformation of plant tannin into gallic acid under solid-liquid fermentation Panda BP, Mazumder R, Banerjee R - J Pharm Bioall Sci

Hyperglycemia, Diabetes and Vascular Disease

[ETD Home...](https://etd.ohiolink.edu/rws_etd)

##### Which is a better area for investing personal effort: curing causes of aging or improving artificial intelligence?
It's a great question, and a complex one. Importantly I know quite a few AI researchers who cite as their main motivation (or a big one) for working in that field the possibility that it could help solve aging. Ben sent me an elaboration of his question that he was unable to include in the question, so I'll quote it here:

---

For a person who is interested in potentially making a large difference, which is a better investment of personal effort, between these two choices-

1. Curing aging-related damage (like the work being done by SRF Home | SENS Research Foundation, run by Aubrey de Grey)
2. Improving artificial intelligence (e.g. to achieve strong AI faster)

I researched this question online and didn't find any discussion on this question (but maybe my Google-fu was weak).

And this is a question about investing *personal effort*, not charitable donations. It seems like the safest choice when it comes to *charitable donations* is to donate to both kinds of causes. I.e. "Diversification is the only free lunch on Wall Street". It's really hard to predict the future, after all, so diversifying donations might be the best way to maximize the odds of helping to create a big difference.

But when it it comes to personal effort on the scientific side, it seems like specialization is key- trying to make a personal contribution in both areas is probably suboptimal. It's very hard to be excellent at two extremely challenging fields.

Some people might naturally gravitate one way or the other, and this way humanity is exploring both options, which is great, since we can't know ahead of time, which is most important. But many young people could go either way, and a choice should be made, and I'm curious what people think is the most promising choice for someone on the fence.

To me, it seems like a person whose top priority is to cure aging, might actually prefer to focus on AI, since maybe strong AI would be the fastest route to figuring out solutions to aging. This seems like a possible two-for-one, if relevant strong AI is more achievable in the near term.

Part of my thinking on this has come from seeing how strong AI compares to humans in games like Chess, Othello, etc.

Aubrey de Grey and I are both familiar with Othello, and Othello is orders of magnitude simpler than the human body. But *even though* Othello is relatively "easy", AI can radically outperform maximum human intelligence when playing Othello (the same goes for Chess, and maybe soon Go as well, given the recent exciting news).

So, I have great hopes for what AI will eventually be capable of.

OR!

It's also possible that focusing on curing aging could be extremely important in speeding up the development of strong AI. This could be due to potential improvements in human intelligence due to understanding biological mechanisms better, or like, if Marvin Minsky had gotten many more years of peak cognition, maybe he (or someone like him) would have already been able to generate a huge AI breakthrough sooner than humanity would otherwise generate it.

Or, perhaps most important, it could convince billions of people to care a LOT more about the development of AI, and how we approach AI when it comes to safety issues, power issues, sharing the wealth, etc., and this would both speed things up and improve the likely outcome.

Does Aubrey de Grey, or anyone else who is a possible expert on how each area might influence the other, have any thoughts on this question? I guess it's a question of "possible timelines, depending on how we invest in each area, and how each timeline influences the other".

Bonus question: which area is easiest to make a contribution in. Is it easier to make a contribution when it comes to biology, or when it comes to artificial intelligence, if a person is starting close to zero?

---

So to answer: well, having worked extensively in research in both areas, I will try to add to the points Ben already raised. First, from the philosophical perspective, I think he is coming from a standard utilitarian position and asking the question as an "effective altruist" as it's often called these days. The impact of progress in each field on subsequent progress in the other one is part of the question, but there are many other dimensions: for example (a) would progress in strong AI be a good thing or would it destroy the human race, (b) can we actually make remotely accurate enough predictions of the amount of impact our time would have to make a rational decision at all, or should we stick to things that have smaller but more immediate and thus predictable humanitarian benefit (this is the position of some leaders in the EA movement), etc. I honestly don't think there is any way to give a strongly defensible answer.

##### Why would telomeres of different chromosomes in the same cell erode at different rates?
There are two known (to me!) reasons why telomeres would shorten at different rates per cell division in a particular cell lineage, and they both simply say that longer telomeres shorten faster. One is that telomere shortening is partly due to DNA damage, and longer telomeres present a bigger damage target. The other is that telomerase acts preferentially on shorter telomeres because there are telomere binding proteins that inhibit it. But obviously, anything that just says longer telomeres shorten faster does not say anything about a population of cells, because it is a negative feedback loop. Perhaps I could say more i you would elaborate on what motivated your question.

##### Aubrey De Grey, in the long run, would nanobots be required to extend healthy life indefinitely?
The only realistic answer (apart from "What counts as a nanobot?") is "Maybe, maybe not". I think it's likely that non-biological solutions to all medical problems, including aging, will play a progressively increasing role in medicine, and that this will be driven substantially by miniaturisation. But whether such technology will ever be absolutely required, we cannot say.

##### Can we use calories restriction on dogs even if we don't know the amount of calories of their food?
Yes, Purina sponsored such a study many years ago. Search PubMed using "lawler df kealy rd " - the 13th hit is the initial report, and the first 12 are all followup analyses.

##### What does Aubrey de Grey think of Alcor Life Extension?
My position on Alcor is very public, so I’m surprised to see this asked. I’m signed up, and I’m also a member of their scientific advisory board (both since 2003 I think). They are, as they have long been, the leading organisation in a movement that does hugely important life-saving work.

##### Could Longevity Escape Velocity happen by 2050 if we donate more to SENS?
I’m looking at more like 2035 to 2040 with 50% probability subject to funding, but it’s by no means certain to be achieved even by 2100, so whatever year from 2035 to 2100 you pick, absolutely a donation will increase the probability. The more specific question is, how much would each dollar help? I do the calculation this way:

- about 40 million people die of aging each year worldwide
- our current budget is around $4 million
- I estimate that we could go about 3x faster if it were $44 million
- that factor will diminish as progress is made and others pile in, but it still probably means a ten-year delay (i.e., with current funding my 50% date is 2045–2050)
- therefore, $40M per year for maybe 10 years could save 400M lives - a dollar per life
- And that’s not even taking into account that this sort of saving of lives is rather more extreme than other sorts, when measured in terms of life years added

##### Is recent research on the cleansing of scenecent cells in mice as relevant as it seems?
Yes it is. This is the best demonstration yet of the value of one of the SENS strands. It is becoming increasingly impossible to maintain the previously almost universal assumption that repairing the damage of aging is far more difficult than slowing down its creation.

##### Of the 7 types of aging damage, which has the highest probability of killing you first?
None - there's no order. They are all held back by different sets of genes, so the selective pressure that maintains those genes over generations depends on all types of damage being bad for physiological performance at about the same age.

##### What is the bottleneck for anti-aging research: money or human capital?
David Gobel is absolutely right: the main thing is that the people with the greatest ability to help are also overwhelmingly people whom a lot of other people respect, and who are keen not to dissipate that respect by publicly supporting a cause that so many people still view as quixotic. But the reason why that matters so much is that the answer to your question as stated is undoubtedly money. The crusade already has absolute world leaders of all relevant disciplines firmly on board to perform the R&D that is needed to get truly comprehensive anti-aging medicine working, but they are paralysed by lack of funds to get on with that job.

Saying that, though, it's still not obvious that the right thing for you to do would be to get wealthy, because generally that takes time. You might make more of a difference sooner by getting to know people who are already wealthy and visionary, and getting them to see past their reputational risk aversion.

##### Why doesn't Larry Page of Alphabet Inc. give Aubrey de Grey's SENS Research Foundation all the money it needs to do what must be done?
An even better question would be "Why didn't he donate a decade ago when Peter Thiel did?" In September 2005 there was a small dinner party hosted by Peter at the Four Seasons in San Francisco, which was the first time the either I or Cynthia Kenyon had met either Peter or Larry. Since then, Peter has funded SENS to the tune of around $6M (though for sure we wish he'd give more!), and Cynthia to a much lesser degree. Larry has gone the other way (insofar as Cynthia is now at Calico). Neither Peter nor Larry has been short of relevant scientific information. So I guess the message is that there is no way to understand the decision-making process of wealthy people.

##### Should the NIH allocate more of its funds to aging research?
Yes or no, depending on what is meant by the term “aging research”. The majority of the $30B NIH budget already goes on research into conditions that mainly affect the elderly, but unfortunately nearly all of that is spent on the quixotic attempt to “cure” specific age-related diseases, in the sense that one cures an infection (eliminating it from the body), which is obviously impossible for conditions that are age-related, since a condition can only be age-related in the first place by virtue of being a side-effect of being alive. At the other end of the spectrum, a small but still respectable amount (around 150M/y) goes on biogerontology research, but again the large majority is devoted to the wrong type of work, namely to increasing our understanding of phenomena that have next to no biomedical potential (most conspicuously, the life-extending effect of calorie restriction or its genetic or pharmacological emulation). Both these errors are fueled by the insistence of virtually everyone (and biologists on both sides of the divide are the most guilty, since they are the ones who should most know better) on the patently false dictum that there is some kind of clear distinction between age-related diseases on the one hand and “aging itself” on the other, when in fact any such distinction is purely semantic. The only chink of light in this sad state of affairs is that a few visionaries within the NIH, led by the head of the NIA’s division of aging biology Felipe Sierra, are working internally to break down this barrier via a vehicle named the Geroscience Interest Group. However, despite the verbal support of Francis Collins (head of NIH), it seems very much as though this initiative will never progress beyond tokenism in terms of redirection of actual dollars, because of the horde of short-termist vested interests arrayed against it and in favour of the status quo.

##### Is aging research more financially constrained or more talent-constrained?
Financially, by a huge margin. Every area that needs effort has the intense interest of at least a few of the world leaders in the relevant fields; they just need the resources to get on with the job.

##### How does parabiosis affect aggregation of damaged proteins/lipofuscin?
I’m not aware of any direct investigation of this issue - but in the absence of that I think we can still say with reasonable confidence that the impact in at least some cell types, such as neurons and cardiomyocytes, would be minimal. It seems that such cells are highly disinclined to do anything, under any stimulus yet explored, that would eliminate such material: they neither divide, nor exocytose it, nor magically activate any hitherto silent enzyme that degrades it. I would be very surprised if any change to the extracellular environment of such cells, which is what parabiosis brings about, would be any different.

##### Is there a unifying factor in aging?
Inevitably it depends what you mean by “factor”. If you mean the question in the narrowest terms, which would be equivalent to “is there a single pressure-point that w emight be able to tweak so as to postpone aging a lot?”, we can be very sure at this point that the answer is no. If you mean “is there an inherent tendency foe the variousconstituent processes that contribute to aging to gravitate to a roughly common rate, as defined by the age at which they start to impair health?”, then the answer is definitely yes (though with the qualification that I highlighted a decade ago when I coined the term “protagonistic pleiotropy”). But maybe you mean something in between.

##### Do naked mole rats have more powerful kidneys than rats? Can kidney parameters explain the lifespan difference between different animals?
Yes and no, in the most useless sense. The two most key things you must always keep in mind about aging and longevity are (1) that in order to live a long time, the organism has to do everything right, and (2) that everything interacts with everything else. Jointly, these things mean that no single component of the organism - whether defined at large scale, such as a particular organ, or at a microscopic scale, such as a component of cells - can play a dominant role in determining the variation in lifespan across species - even cross closely-related species, like naked mole rats versus mice. But they also mean that no component that actually does anything can play a zero (or even negligible) role. The only things that can play a negligible role are things that don’t do anything - which is, of course, what SENS focuses on, namely the various types of life-long accumulating damage that the body does to itself in the course of its normal operation. The reason why that makes sense is that damage only temporarily doesn’t do anything; eventually there is enough of it to get in the way.

##### How far are we from being able to extend the lifespan of a mice to 10 years?
Quite a long way - probably, I’d say, further away than we are from reaching longevity escape velocity in humans. The problem is that mice are shorter-lived than humans for a reason, or more precisely for a whole host of reasons: in a nutshell, their in-built anti-aging machinery has bigger gaps in it than ours does. That means it’s harder to plug all those gaps well enough to make a several-fold (which is what you’re describing) difference to lifespan. I think we have a good chance to get mice to five years within under a decade, and that’s even with interventions started in middle age; but getting to ten years is a far bigger leap from that than it may sound. Conversely, getting humans to 150 is 90% of the work to get them to 1000, because plugging most of these gaps (i.e., enough to get anything much at all) is a lot harder than in mice, not least because we’d be a lot unhappier if 10% of the humans were inadvertantly killed than if 10% of the mice were. Counterintuitive, I know, but pretty obvious when you think through the above.

##### What would be needed to change in our organism in order for us to be immortals?
Nothing. All that is needed in order to eliminate the rise with chronological age in our risk of death in the coming year (which is what I am going to presume you mean by being immortal, though I strongly disapprove of that word being used in that way) is to develop medicine to repair the self-inflicted damage of aging faster than it is being created. That’s what SENS Research Foundation is doing. Some of our work may lead to therapies that are “one-off”, i.e. they really are changes to the organism (typically the addition of genes), but even those probably won’t really be one-off, because gene therapy won’t hit every cell.

##### What are the most important human aging related AGEs after glucosepane?
That is a hugely important question - especially since the better way of phrasing it is “how sure can we really be that there are not in fact other ECM modifications that are even more important than glucosepane in contributing to aging?”. The short answer is: nowhere near as sure as the literature implies. The long answer falls into four parts.

1) Are there non-crosslinks that matter? There are of course lots of AGE non-crosslinks, such as carboxymethyllysine. My belief has always been that such adducts are basically harmless at the levels that accumulate in a currently normal lifetime - an example of protagonistic pleiotropy arising from their pathway of formation (and thus the genes that suppress their formation) having so much in common with those for crosslinks - but I might be wrong.

2) Are there non-AGE crosslinks that matter? There probably aren’t any that are formed non-enzymatically: the best-known example is dityrosine, which for sure is less abundant than glucosepane, but we must keep looking. But there are reports that a well-known enzymatically-generated one, EGGL, increases with age, and it is unclear whether this is a result of a shifting dynamic equilibrium between creation and destruction or whether there is just no destruction. In the latter case, EGGL would need to be addressed, even though it’s not an AGE.

3) Are there known AGE crosslinks that are of comparable or greater abundance than glucosepane? Definitely not in human collagen, but we must not forget that there are other ECM proteins that have been studied less well. The only real candidate right now is K2P, a lysine/lysine link that is very abundant in the lens; this is probably a weird special case caused less by the fact that the protein (crystallin) is not collagen and more by the very high ascorbate concentrations.

4) By far the scariest option: are there bona fide AGE crosslinks that accumulate more rapidly with age than glucosepane but have escaped detection? We have been funding an outstanding group in the UK, that of Jonathan Clark at the Babraham Institute, to work in partnership with our Yale group (that of David Spiegel), and their focus has been exactly this question. So much of science is limited by only seeing what you are looking for, and the more we examine the methods that have been used to analyse aged ECM the less confident we become that nothing has been missed. After all, glucosepane itself was missed for a very long time. And the very bad news right now is that we are desperately short of funds, so Jonathan’s work is currently on hold. We badly need to resume it. Our recent donation from Michael Greve (see SRF Home for details) will match any other donation for this project (and for most of our other projects), but we still need to actually obtain those other donations.

##### Is aging a body's attempt to prevent cancer?
For some bad definitions of aging the answer would be “mostly yes”, but for good definitions of aging the question doesn’t make sense, because nearly all cancers are parts of aging. Most cancers predominantly affect people who are chronologically elderly, because they arise from the lifelong accumulation of damage to a cell’s DNA, arising as side-effects of normal metabolism, that enables it to resist the body’s many anti-cancer mechanisms. And anything that results from the lifelong accumulation of damage rising from metabolism should be viewed as part of aging, whether or not we give it a disease-type name.

##### Can we live until 200 if we clear AGEs, amyloid, senescent dells, and if we inhibit atherogenesis? Would it be enough?
No it would not. For a start, none of those measures would postpone cancer even by a decade. See SRF Home for a more thorough answer.

##### Can IT progress like more speed and deep learning accelerate the anti-aging progress? For example, move the LEV from 2050 to 2035?
You mean the Methuselarity, i.e. the point at which we reach LEV. I already put that at having a 50% chance of achievement by the late 2030s. But to answer the substance of your question, my answer is a little complex and revolves around the messy and incremental manner in which I am pretty sure the initial transition to a post-aging world will be implemented. Basically what will happen is that a wide range of damage-repair therapies will be implemented, they will each kinda work, and they will each substantially postpone the ill-health of a subset of people (the people who are accumulating that type of damage a little faster than other types) and slightly postpone the ill-health of a lot more people, the ones who are getting other types of damage up to a pathogenic level at about the same time, by virtue of the plethora of knock-on effects that exist (the interaction between systems within the body). The damage repair itself is probably not going to be much accelerated by clever algorithms and big data, in my view, because we basically already know what to do and the rate-limiter (unless you count funding for the research, which is very definitely the rate-limiter today) is the scientific process, the grinding through discoveries of technical details that we don’t know. But the situation is different for the knock-on effects: they vary quite a lot in magnitude from person to person, as a result of innumerable details of metabolic variability, so in that area I think that big data and deep learning and so on have a substantial chance to identify personalised optimisations that amplify the effects and thereby postpone ill-health by a greater amount. And yes, that means hastening the Methuselarity. Probably only by a few years, but those will be very welcome years.

##### Do you know of any viable and robust criticism of SENS research project?
I’m intrigued by both the answers given by others so far - for different reasons, unsurprisingly. Duane’s reply makes little sense to me because we focus very strongly on rejuvenating the immune system: indeed, in my original formulation immune senescence was its own category before I realised that it was better described as subsumed within cell loss and cell death-resistance. Nathan’s answer is actually not so much intriguing as enlightening, to others if not to me, since it expresses very honestly the difficulty that so many basic scientists have in appreciating the difference between science and technology. For a technologist, the fact that we don’t yet know (despite decades of work) whether protecting mtDNA will slow aging (or, more precisely, will be a necessary component of a panel of therapies that jointly slows aging) is of little importance: if it might slow aging, and it seems to be hard to determine whether it will, and we have a fair idea how to do it, let’s just go ahead and develop a way to do it, and if our achievement ends up being unnecessary in the end, no harm done. Whereas, if we spend another few decades trying to figure out whether mtDNA damage matters and not developing ways to fix it, plenty of harm may be done, because we may fix everything else and thereby find out the hard way that yes mtDNA damage matters because people keep getting sick and dying on schedule. But this way of thinking is completely alien to basic scientists who find things out for the sake of finding things out. Conversely, technologists like myself are intensely frustrated by the fixation of basic scientists on phenomena that have long ago been shown to have minimal potential for humans (calorie restriction being the main one) resulting from the terribly interesting things that such interventions do to lab animals.

To answer the actual question: no. SENS has evolved in terms of its fine details, as new technologies such as iPS and CRISPR have come along, but the overall structure is still abundantly standing the test of time.

##### What does Aubrey de Grey think of minimal cells like JCVI-syn3.0 Minimal Cell?
They are a formidable technical achievement, but there is no knowing at this point how useful they will be in the development of future medicines etc. The first things to come from them may be improved understanding of metabolism, arising from identification of the function of the many essential genes whose function is currently completely unknown.

##### What does Aubrey de Grey think about MitoQ?
I think mitochondrially-targeted antioxidants are very worthy of more study. If anything can make antioxidants really work toslow down the creation of aging damage, it's these. But, I still think the jury is out as to whether they actually can. I was quite disappointed at Skulachev's failure to extend maximum mouse lifespan with his version of the same idea - I rather expected the result to resemble what happened with mitochondrially-targeted catalase (Schriner et al from a decade ago).

##### How is SENS research on longetivity different from Calico (owned by Google)?
Calico are being quite tight-lipped about their activities (as most private companies that don't need to raise money tend to be!), so to some extent one can only guess. But from their pattern of hiring, it's a good bet that they are focusing on trying to understand aging better, as a step towards figuring out how to postpone it. That's not surprising when you have a chief science officer (David Botstein) who is on public record that he doesn't have a translational bone in his body, but it's unfortunate, because the field has moved on from that attitude and it is now entirely orthodox to think in terms of intervention based on what is already known about aging, i.e. without finding out any more fundamental truths. We have of course tried to educate them on this, but thus far they have basically blown us off.

##### How can an expert in molecular simulation (molecular dynamics, Monte Carlo, etc.) help defeating aging and implementing SENS?
There are a few options, but they depend on your specifics. Best thing is if you email me at aubrey@sens.org and I'll get one of my colleagues to reply thoroughly.

##### What is Marc Tatar known most for doing within the biology/aging community?
He's a very strong cyclist - probably surpassed only by Siegfried Hekimi, who rode in one or two Tours de France in his day. He even ships his bike to conferences in the Alps and such like.

##### How does one break up Carbamylated Proteins?
We're looking closely at this new discovery, but let's be clear that at this point there is no evidence that this type of modification leads to crosslinking. It remains to be seen whether it matters at all.

##### What does Aubrey de Grey think of Ray Kurzweil's prediction about Longevity?
In a nutshell, we’re not all that far apart. We differ somewhat as regards what can already be done today (what he calls “bridge 1”), but regarding future advances we are on very much the same page.

##### Using cutting edge science and almost infinite funds, can we keep a human head alive for longer than normal human lifespan?
Absolutely not with today’s technology. Also, realistically it is very unlikely that the “autonomous” aspects of brain aging are unimportant enough that a brain’s aging could ever by substantially slowed down just by connecting it to a young-like blood supply. We’ll fix aging in general, brain included, before then.

##### What does Aubrey de Grey think of Maximum Human Lifespan, which seems to be about 115 years?
If you’re referring to the recent paper in Nature from Vijg’s lab, I have some issues with the statistical methods used but I agree with the conclusion. However, please understand that the conclusion says NOTHING AT ALL about what may be achievable with future medicine. It is all about how ineffective present (and past) medicine has been in alleviating aging.

##### What does Aubrey de Grey mean by “Aging is a phenomenon of physics, not biology”?
I mean simply that the underlying reason why complex living organisms age is the same as why man-made machines with moving parts age, namely that the laws of physics dictate that wear and tear happens and that it takes work to reverse the accumulation of that wear and tear.

##### If Aubrey de Grey was going to college this year, what would he have studied to become a researcher on aging? Does he think MD is an alternative?
I would recommend a general biology degree course. Aging affects the body at every level of organisation, so in order to understand it well one needs a good grounding in genetics, biochemistry, cell biology, molecular biology, physiology, the lot. An MD is not such good training because it mainly emphasises what we can already do today.

##### What organizations exist with similar missions as SENS?
If one defines our mission as the medical control of aging, there are (gratifyingly) a large and increasing number, both for-profit and non-profit. If one defines it more narrowly as the application of the SENS concept of damage repair/obviation to the molecular and cellular constituents of aging, so far there are none that take it on as a general mission, but there are now a few that are focused on specific examples of it. These include spinouts from SENS Research Foundation, such as Ichor , and also independent companies such as Unity. The rejuvenation biotechnology industry, which it has always been SENS Research Foundation’s goal to engender, is finally emerging.

##### Can Quercetin or drugs that use apoptosis induction increase health span in humans by killing senescent cells (that spread cytokines)?
We can’t know the answer to that until it is tried, but the preliminary evidence from rodent studies is promising. The other, necessary, big question is whether such drugs can be sufficiently selective so that they don’t also kill cells that we want to keep. If that turns out to be very hard, the alternative is to be more sophisticated and use genetic rather than pharmacological targeting. This is the approach that I have always advocated within SENS, and it is now being pursued by a new startup named Oisin that we work closely with.

##### Has Aubrey de Grey's knowledge of computer science made significant and concrete contributions to his research on aging?
A huge contribution, especially early on after I switched fields. Actually, to be more precise, it was not so much the knowledge as the way of thinking that is typical of CS, which is totally unlike what is typical in curiosity-driven fields. CS, being a mainly goal-directed field (a technological one rather than basic science), uses evidence very differently. And in the mid-1990s, the problem of aging was ripe to undergo the transition from discovery into translation (a transition that is still in progress, don’t get me wrong). I was in the right place at the right time for my skill set.

##### Is aging due to accumulation of malfunctioning cells or due to cell depletion?
I don't have much to add to Kurt's answer, which you don't seem to like. I don't understand why you are convinced that the problem of aging has to be too much apoptosis or too little. As Kurt says, sometimes it is one, sometimes the other, and sometimes neither. It just depends which cell type and which organ or tissue you are looking at. In SENS, too much apoptosis (more precisely, too little cell replacement) and too little apoptosis are two of the seven categories that I partition the many types of damage into, for the purposes of describing ways to repair or obviate that damage and thus maintain youth.

##### Why do telomeres matter in post mitotic c elegans?
Well, what exactly do you mean by "matter"? C. elegans are not completely postmitotic - they obviously have dividing cells in the germ line.

##### Does SENS Research Foundation have plans to start collaborating with, or to collaborate more closely with Calico, Human Longevity Inc., and/or Alcor Life Extension Foundation?
Calico: we hope so, but they have basically blown us off so far. They are being quite secretive about their plans, but from the range of people they are hiring they have not yet really got the message that damage repair is the way to go.

HLI: maybe, but the connection is less obvious there, because HLI are not (yet!) really in the business of defeating aging entirely; instead they are seeking to improve personalised medicine by sophisticated use of genomic sequence data.

Alcor: yes and no. I've been on their SAB for a decade but we don't work directly with them. However, their ex-CEO Tanya Jones, who was for five years our COO, is now CEO of a hugely exciting startup named Arigos (along with Steve Van Sickle, who preceded her as Alcor CEO) - they are working on a new method of cryopreservation that has huge near-term potential in the organ preservation market as well as being a potential game-changer in cryonics per se. We invested in Arigos when they set up.

##### If you want to hasten the anti-aging research, why should you donate to SENS Foundation instead of others organizations?
Thanks for the question, and to Tony for his very thorough reply. I don't have much to add, actually. SENS is a bona fide plan for defeating aging entirely, by repairing the accumulating damage that eventually kills us. Almost all other approaches entail, in one way or another, slowing aging down by taking advantage of the genetic machinery that underlies the response to famine. That concept used to seem really promising, as a result of the impressive life extension demonstrated both by famine itself and by its genetic or pharmacological emulation in laboratory organisms, but for a long time it has been obvious to anyone who was really being objective that such an approach would probably work far less well in longer-lived species (I wrote a detailed paper to this effect in 2005), and we now have conclusive data to prove it in the form of the two huge monkey calorie restriction studies that concluded in the past few years. It's therefore downright scandalous that people who should know far better are still pursuing that approach. Another approach is to optimise the effect of medicines that apready exist, using improved knowledge about individuals' genones and other omes - that's what Craig Venter's HLI is doing, basically - and again it's only going to have modest benefits at best.The other big reason to fund SENS Research Foundation is that some other organisations are indeed focused on damage repair, but only on the lowest-hanging fruit that will either make money or get publications really quickly. We respond to that by doing the opposite - prioritising the equally vital but hardest and thus most neglected areas. It definitely pays off - for example, six weeks ago we had our first publication in Science, arising from the work on crosslinking that we fund at Yale - but it takes a long time to do so, so it needs donors with just as much vision and patience as we ourselves have. And there sure aren't enough of those. My current estimate is that we are being slowed down by as much as a factor of three at present by shortage of funds, and that's in grave danger of getting worse soon, when the funds I donated in 2011 from my inheritance run out. So all in all, I believe we've made a strong case for being the right beneficiary for any donors who want themselves, their loved ones and humanity in general to stay truly heathy however long they live.

##### Could CRISPR be used to promt macrophages to 'clean up' atherosclerotic plaques?
Probably not on its own, because we think it is necessary to introduce new genes (from other species, probably bacteria), which CRISPR isn't designed for. But there is the alternative of doing a bone marrow transplant with genetically modified stem cells, which will enhance a subset of the subsequent macrophage population.

##### Is it within the realm of possibility that someone could be born with a genetic mutation that led to longer life...?
No, but the reason why not is subtle enough that you could certainly get away with it in fiction. There are mutations that confer 30% or so life extension in mice, but the overwhelming preponderance of both evidence and theory is that such mutations confer much less life extension in longer-lived species. (This inconvenient fact is assiduously swept under the carpet by a depressingly high proportion of the researchers who work on those mutations, but hey, their hands are tied as they have each other's grant applications to approve...)

##### How promising for Alzheimer's are the amyloid beta disrupting drugs from Eli Lilly and Biogen as of September 2015?
I'm very hopeful, but only because of what's coming. The clear message from the trials is that amyloid matters when it's the predominant issue but not when it isn't (well duh). To elaborate - the Biogen trial succeeded because it specifically recruited patients whose Abeta load was unusually high for their level of cognitive impairment. Tangles matter too, and maybe the earlier trials failed because too many of the patients were mainly suffering from tangles. Short story, this is aging in microcosm - a condition arising from the combination of multiple typesof accumulating damage. 

So, why an I hopeful? Because tau immunotherapy is coming! Tau moves between neurons, and there is pretty good evidence now that it can be grabbed by antibodies en route. It's early days... but I think this could be the area in which the value of combination therapies finally hits a home run. 

I expect that patients with fairly advanced (though not terminal) AD will benefit quite a lot from the removal of both tau and Abeta, in contrast to what we see with only removing one of them which is that only mild patients get any meaningful benefit. But but but, this all depends on the companies being sensible and not pandering to the drive for simplicity. I don't think removing tau on its own will do all that much better than removing only Abeta.

##### If we believe that we can slow or halt aging the future, would it be possible to reverse aging for people who were older at the time that such technologies were discovered?
Absolutely yes! - the whole of SENS is about damage repair, which is not exactly the reversal of the processes that created the damage, but is identical in terms of the outcome - one would be restored to the physical and mental performance of a young adult. Concerning DNA, there are various answers. One part of SENS entails putting backup copies of the mitochondrial DNA into the nucleus, so that mitochondria will always work whether or not their DNA is damaged. Damaged DNA can also be replaced just by replacing the cells that contain it, and I believe that until we have extended longevity many-fold we will probably get away with restricting ourselves to curing cancer, because other mutations don't accumulate fast enough. And if we want to look really far ahead, we don't have to worry about not having stored cord blood or whatever, because we can "average" the damaged DNA - no single mutation will be present in a majority of cells (or anything close), so we can just swap out sequences that we find only occasionally in favour of the majority sequence, without needing to know what the mutation did. (Of course this is rather easier said than done, but I did say "really far ahead"!).

##### Is [this article](http://www.bloomberg.com/news/features/2015-02-12/does-a-real-anti-aging-pill-already-exist-)a fair portrait of state-of-the-art anti-aging pharmaceuticals? Why, why not?
Well no, clearly not, since it's only about rapamycin. But as far as it goes it'sa fine article, yes.

##### Aubrey de Grey I've been studying aging for almost a decade now, and I'm a biochemist. I think the best approach to overcome aging is to have a whole-body replacement strategy, rather than repairing body. What do you think about this strategy?
There's not so much difference between replacement and repair as you're suggesting. In many ways the difference is purely semantic, revolving around the scale at which you're describing the procedure: in a car, for exampme, replacing the engine constitutes repairing the car, and replacing the spark plug constitutes repairing the engine, etc. Sometimes the scale that is practical will change over time - initially it may be easier to replace the whole heart with one built in the lab, for example, whereas later it will be easier to repair it by replacing individual cells and clearing our waste products and so on.

##### Does Aubrey de Grey have any opinion about the ketogenic diet?
Not really - diets are not my area of expertise, because what we can say for sure is that no diet seems to confer anywhere near the impact on aging that SENS seeks to achieve.

##### What does Aubrey de Grey think of the creation of Google Alphabet?
I'm not sure that there is all that much to think. It seems to me no more nor less than it is being stated to be - a reorganisation of their top-level organogram to reassure shareholders. As such, it seems like a good thing in that it insulates the more visionary entities like Calico.

##### What will the effects of life extension technology be on overpopulation? What models exist to predict population dynamics?
See this recent paper reporting the initial results of a project we funded to explore exactly that question (and related economic and political ones):

[Opportunities and challenges of a world with negligible senescence](http://www.sciencedirect.com/science/article/pii/S0040162515001985)

##### Why is Aubrey de Grey not raising funding for SENS through Crowdfunding?
We have used crowdfunding a little, and we're planning to ramp it up, but we don't see it as having the potential to make a big difference to our budget any time soon. The basic problem is that all our projects need six-digit sums annually, and that they don't have clearly defined timelines or deliverables. Of course they can be carved up into small subprojects that do, and whose costs are smaller, but then the problem becomes one of being inspiring: the subprojects are necessarily rather technical and hard to make attractive to the masses.

##### Do rates of biological ageing less than zero exist in humans? What does it mean?
They could indeed have been recovering from health issues, or else it could be a result of the unavoidable noise in the experiment - variations in parameters due to time of day, amount of sleep the person got the previous night, whether they were under psychological stress, a million things. More generally, my take on this study is that it is a very tantalising but extremely preliminary foray into the challenging area of longitudinal study of aging in early adulthood. A great start, but only a tiny part of the puzzle.

##### Is the creation of the Alphabet Holding good news or bad news for the long term plans of (Google) Calico?
No. I'm 99% sure it is purely a measure to soothe Google shareholders and will make no meaningful difference to the activities or fortunes of any of the components, including Calico.

##### What can I do to live as long as possible?
Your best bet is to give SENS Research Foundation lots of money, so as to hasten the development of medicines that will bring aging under genuine medical control, and thus to increase the chances that that will happen in time for you. Failing that, persuade other people to do so.

This is not a flippant answer. While all the things that others here have recommended have some value, for most people the effect on lifespan will be tiny. The only way to live even a decade longer than you otherwise might is to benefit from future medicines.

###### Comments
- Hannes Hoffmann: While the things others have recommanded probably do not make people die a lot later, i think they make them die healthier. So in case your chance to benefit from future medicine depends on your state of health in 20 or 30 years, leading a healthy live now might be important for livespan.
- Aubrey: Actually even that is only marginally the case. It's true that people who live the longest also tend to have the shortest period of disease before they die, but the bulk of that correlation is due to the short-lived and least healthy end of the spectrum. In other words, there is a big difference in both healthspan and lifespan between living averagely and living unusually unhealthily, but a very small difference between living averagely and living unusually healthily.

##### What has improved or changed since 2007's Ending Age book was released? Are there new advances in any of the researches that the book mentions? Has the approach for any of the 7 lines of action changed, evolved or advanced?
There have been many big advances, yes, both in our own work and in independent work - see our annual reports, our newsletter (subscribe!) and our news updates at [SENS Research Foundation](http://sens.org/) for details. Arguably even more heartening is that no, there have been no major updates in our approach as a result of new discoveries - it is robustly standing the test of time. There have essentially only been good surprises, i.e. advances that have given rise to short cuts, making one or another SENS strategy easier than we thought it would be.

##### What does Aubrey de Grey think of 2045 Initiative?
Neither, actually: I just think SENS is closer to being achieved. I could be wrong, though, so I strongly support Dmitry's efforts - if uploading gets to work before SENS does, I'll be in the line for it. Dmitry feels the same: what matters is to save lives, not how it's done.

##### Assume that projects led by either Dmitry Itskov or Aubrey De Grey succeed in significantly extending human lifespan. How likely is it that politics and legal issues will cripple the rise of immortality on trivial grounds for several years?
There is no chance at all that any of these arguments for restricting access will prevail. The universal desire to remain healthy will dominate; it will be impossible to remain in power if one opposes, or even is neutral about, the delivery of that technology to one's people.

##### Has the life span of a particular blue whale been monitored? How much was it?
Bowhead whales are generally thought to live even longer than blue whales.

##### Can transcriptomics be used in lieu of lifespan studies to determine if an intervention slows or speeds aging?
Depends what you mean by "aging". It's easy to come up with reasonable definitions of aging that make the answer to your question obviously yes or obviously no.

##### Is the TA-65 yet proven to be effective in lengthening telomeres in humans?
My information is that yes, there is clear telomere elongation. Whether that is a net positive for postponing age-related ill-health remains an open question.

##### If there is a major breakthrough in aging research that can increase life expectancy by at least 5-10 years, how long will it take to verify it?
The first thing to remember is that the life extension effect will be merely a side-effect of postponing ill-health. This means that the time it takes to verify it and convince people also centres on health; people won't need to be convinced of the life extension effects, because they already just don't like getting sick. Second, the time taken will depend on how the therapy works - specifically, on whether it repairs the damage of aging or only slows down the further creation of that damage. The latter takes a lot longer to verify;  the good news is that repair will almost certainly be easier.

##### What do Matt Kaeberlein and Aubrey de Grey think of each other?
We don't actually know each other all that well. He's an excellent scientist. I don't really know what he thinks of my science, but I strongly suspect he is not so dismissive of it as the 2006 critique of SENS that his friend Pete Estep somehow persuaded him and half a dozen other researchers to sign.

##### Does Aubrey de Gray make a valid point about reversing aging in the coming decades?
Sanjay - what parts of my publications on this topic do not sound strongly fact-based to you, exactly?

##### Why are so many mainstream researchers in aging skeptical of Aubrey de Grey?
The main reason for the residual resistance to SENS among mainstream researchers is fear of association with the idea that radical life extension is foreseeable. The problem is outlined in my most recent editorial in Rejuvenation Research:

[Longevity Sticker Shock: The One Remaining Obstacle to Widespread Credentialed Support for Rejuvenation Biotechnology](http://online.liebertpub.com/doi/abs/10.1089/rej.2015.1732)

##### What does Aubrey de Grey consider to be the strongest argument against ending aging?
As Johnty predicted, my answer is that there is no remotely strong argument against ending aging.

###### Comments
- Issa Rice: This isn't an answer. "Strongest" doesn't mean "strong"; it means "strongest out of all the arguments, even if they are all weak".
- Aubrey: Indeed - but "not remotely strong" means that all arguments are so ridiculously weak as to be unrankable.

##### Do you expect cancer immunotherapy to significantly increase the human lifespan?
Not on its own, no, simply because the complete edarication of all cancer would not - it would only add a couple of years. This is a simple mathematical consequence of the fact that a lot of life-threatening conditions rise exponentially in incidence with age, all of them by roughly 10% per year; since "only" 20-30% of people die of cancer, that means it only takes a couple of years for the total incidence of all the others excluding cancer to overtake the total including cancer.

##### Why is the average human life expectancy increasing?
The main thing that I don't think has been said yet is why life expectancy in the developed world has continued to increase even though the impact of hygiene, vaccines etc has long reached diminishing returns. Basically, the reason is "cohort effects" - improvements to health early in life that keep people healthier at a given chronological age than people born earlier. The main cohort effect is probably early-life (including prenatal) nutrition. In other words (for illustration), because on average people born in the West in the early 20th century were in more prosperous and thus better-fed families than people born in the West in the late 19th century, they were "born younger" and stayed biologically younger than the older cohort throughout their lives, with the result that they lived longer.

##### How much will joining the Methuselah Foundation's "300" actually accelerate longevity research?
Here's how I measure it. I estimate that there is a 50% chance that we will achieve a decisively comprehensive level of medical control over aging (what I've called "longevity escape velocity") within 20-25 years, so long as we are not slowed down by lack of funds. I also estimate that at present the lack of funds is slowing our rate of progress by a factor of about three. That factor will fall over time, since the main thing causing lack of funding is lack of progress - each small step forward pushes a few more people over the edge into thinking it's a worthwhile venture - so at a rough guess I think that we will lose about five years in the long run if funding stays low for the next ten years. (I estimate that after 2025 the amount of progress we've made even with low funding will have been enough that there is unlikely to be all that much trouble getting the necessary funds.) The level of funding I think we would need in order to eliminate those five years is about $100M per year, as against the current level of $5M per year; however, because we (obviously) prioritise the most impactful projects, the first additional $1M would make at least twice as much difference as the last one. Each year, roughly 40 million people die of aging worldwide. So, combining all those estimates, one gets a number of roughly $2 donated today per life saved, which compares very favourably with other ways of spending money (and of course the definition of "life saved" is rather stronger than it is for other medical interventions, since it entails adding a lot more to the recipient's healthy and total life expectancy).

Note that the above is written in terms of donations to SENS Research Foundation, the charity of which I am now the Chief Science Officer, as opposed to our sister charity the Methuselah Foundation, which I co-founded and which (as the question notes) is the one that has the "300" club. We have identical missions, but by and large SRF is the one that does and funds research, whereas MF is the one that runs prizes.

For anyone who is wondering why organisations involved in the "effective altruism" movement are not advocating more strongly that donors should support SENS: the main reason is that there is a lot of skepticism within such organisations concerning the ability of researchers to estimate the difficulty of their research. GiveWell, for example, talk a lot about the value of such research and about their intention to get more active in that area, but in the end they still only recommend charities that help the developing world. There is a lot of debate within that community concerning whether this is a valid policy. For example, see this piece by Peter Singer:

[Should We Live to 1,000?](http://www.project-syndicate.org/commentary/the-ethics-of-anti-aging-by-peter-singer)

##### If all SENS objectives are realized would humans be eternally in their 20s?
Basically yes, both mentally and physically (except that of course SENS would not erase one's memories of adult life!). Better, well, there might be some such side-benefits, yes, but they would mainly arise from secondary uses of the technologies.

##### How long will it take for anti-aging technology to reach escape velocity under current SENS funding?
That depends on how long one expects the funding to stay at current levels. At present I think we could be going roughly three times faster than we are if we had $50M per year to spend rather than only $5M. But as we make more progress, it will inevitably become easier to raise more funds. Taking all such things into account, I currently estimate that if we jumped to he $50M/year level tomorrow we would have a 50% chance of reaching LEV within 20-25 years, and every three years that go by with funding staying stagnant adds two years to that number.

##### What, in your opinion, is the most likely technology/medicine to dramatically change the way we age?
See http://sens.org/ for my answer, obviously...

##### Do mice with mega-telomeres live longer?
No. Telomeres play a very different role in the trade-off between different potential causes of age-related death in small mammals versus large ones. Check the work of Woody Wright and (independently) Vera Gorbunova on this.

##### Aging: How is the The Longevity Fund different from the SENS Foundation?
Well, the Longevity Fund is a venture fund focused on supporting companies working to postpone age-related ill-health, whereas SENS Research Foundation is a biomedical research charity focused on funding in-house and university-based research projects to postpone age-related ill-health. So we're in the same field, and the same part of the world, but our methods are complementary. Laura Deming and I are good friends though :-)

##### What can someone do to live forever? I've read about parabiosis. Would younger family members donate their compatible blood to be used in elected infusions? Would a clinic agree to that, or would health care professionals decry it as unethical?
Evidence is accumulating, not least from the parabiosis work you mention, that significant rejuvenation may be possible via restoration of youthful levels of certain factors in the blood. However, as noted in another answer here, there will certainly be aspects of aging that are not affected by such procedures, and since ultimately you are as old as your weakest link this means that more is needed in order to postpone ill-health substantially. And unfortunately, a lot of that "more" is still in the early stages of development (not least by SENS Research Foundation).

Thus, depending on exactly what you mean by "advanced age", I don't have the sort of answer you're probably looking for. There is nothing available today that can get someone to what I've termed "longevity escape velocity", and there almost certainly won't be for at least another 20 years. I do very much advocate signing up to be cryopreserved, because that really is a lifeline - and an increasingly strong one, as research progresses in solving the key challenges inherent in minimising the damage done to tissues by the cryopreservation process. But mainly what I advocate is not focusing too strongly on oneself. As a 52-year-old who is dedicating his life to this cause, I can tell you that what gets me out of bed in the morning is not the thought that my work is incrementing my own chances of making the LEV cut by a percent or three. It is that my work is saving a ridiculous number of lives - getting others to make the cut, whether or not that cohort includes me. I don't know whose lives I'm saving, because I don't know how soon these therapies will arrive, but I do know how many lives - over 100,000 for every DAY that I hasten the defeat of aging. The same applies to money as to time, of course: based on my current estimates of how much the lack of funding is slowing down critical-path research, I calculated recently that it only costs $3 to save a life by contributing to this work.

##### What is a reasonable estimate as to the degree of longevity extension that could be realized via stem cell therapy alone?
I would be very surprised if we got more than five years that way - in fact I would guess no more than two years. The way to calculate this is to list the major killers that would not (as far as we know) be significantly delayed by stem cell therapy - which, unfortunately, include both atherosclerosis and cancer. That kind of logic is why SENS Research Foundation has elected to go the route of diversity, addressing everything that underlies every cause of death whose incidence rises exponentially with age.

###### Comments
- Lucas Karl Hahn: I remember reading in your book something about replacing cells with stem cells every 10 years or so to stop both aging and cancer, I think it may have been called WILT. Is this different from stem cell therapy?
- Aubrey: Close but no cigar. First, there's no such thing as "aging and cancer" by my definition, becaue cancer is part of aging. Second, WILT is not to stop both [non-cancer aspects of] aging and cancer, it's only to stop cancer. Third, WILT entails not only stem cell therapy but also gene therapy to remove cells' ability to extend their telomeres even if they mutate a lot. Read Chapter 12 again!

##### Is Elon Musk right when he says that the agreement of geneticists to not reprogram DNA could hamper anti-aging efforts?
Well, first let me note that this is the first time I've seen any remark from Musk concerning the defeat of aging. I've met him, but only once, years ago. From what is written in the interview, I infer that he has a good understanding of the basic nature of the problem (specifically that it is a chaotic one that will only yield to a divide-and-conquer solution) but that he has not spent much time learning about current efforts to solve it. His remark about reprogramming DNA suggest that he has not yet seen past the idea of germ-line genetic engineering to turn us into a species that is still in essential ways human but yet doesn't have aging any more - which is grossly oversimplistic, but I don't mean that harshly, as it's a fine place to start when you don't yet know much biology, still less much biogerontology. I'm hoping that one day he will become curious enough about all this to get more informed and involved - but as is mentioned, he's quite busy doing a lot of other very valuable things already. Luckily, others of his ilk (notably Peter Thiel) are prioritising aging already.

##### To what extent, if any, does SENS Research Foundation watch for non-7-Causes longevity discoveries? (see details)
We absolutely watch for such things. Let me restate your question a little though. One thing we watch for is additional causes - eighth types of damage. We can reject them because of compelling evidence that they accumulate too slowly to matter in a currently normal lifetime; sometimes we need to do research to obtain such evidence, as with our project on epimutations at Einstein. The other reason for rejecting them is if there is compelling evidence that they will spontaneously reverse if we fix the existing seven. But your question is not with regard to new types of damage, but new types of fix. The question then is whether the fixes work by somehow overriding the seven damage types, or by fixing them, or by fixing an eighth damage type that we haven't yet characterised. To take the examples you cite:

The one about heterochromatin is a hot topic right now. It's closely related to our work at Einstein mentioned above. But this particular study tells us very little, because it's in a model of accelerated aging - it's easy to make cells or organisms unhappy at a younger age than usual, and that doesn't mean they get unhappy for that reason in normal conditions. As things stand, Im still betting that these changes happen too slowly to matter in a currently normal lifetime.

The one about blood infusions is of the other type. For sure the blood change sin composition in many ways during life, and those changes act to spread aging around the body - basically, to accelerate the aging of tissues that are doing relatively well, by exposing them to the problems of tissues that are doing relatively badly. But clearly if we can properly rejuvenate the latter class, the blood will come right on its own. Conversely, if we do this kind of infusion, yes it will have some benefit, but as the problematic tissues get older and older it will be less and less effective.

##### How promising is the ultrasound Alzheimer's treatment shown in Leinenga and Götz's March 2015 article?
It's definitely intriguing, and I agree with Jae, we need to know about the long term. If microglia can do this, why do they not do it already? The good news is that we are already pretty much there in terms of removing plaques using vaccination, so the focus has really turned to removing tangles and replacing lost neurons and reversing synaptic atrophy.

##### Why do we age? How does the aging process work? What can be done to stop the aging process?
See http://sens.org/ and my book Ending Aging.

##### What would it take to reverse presbyopia?
Basically just a crosslink-breaker that would restore the lens's elasticity. The molecular structure of lens crosslinks may not be the same as in collagen etc elsewhere in the body, so this may be some way off.

##### Does in-silico testing and development as mentioned in the video below seem like a prime candidate for the most fruitful avenue to pursue in the coming decades for disease and aging research and intervention?
"Candidate" is the wrong word - "component" is the right one. We will achieve proper control of aging by combining many technological advances: we need breakthroughs across the board. I'm quite sure that better ways to analyse large datasets will play a substantial part in that, and that's what this company are doing. I think they're doing it in a very promising way. Also, I think its contribution will become clear within a matter of years, not decades.

##### Do Cenegenics programs really work?
Before one can answer such a question, one needs to define the criterion. What do you really mean, quantitatively, by "it works"?

##### Based on the growing advancements in medicine and technology now and in the future, what is the predicted life expectancy of a 30-year-old?
Can't be predicted, because it depends on so many things - how safe cars become, how well we avoid asteroids, etc. First things first - aging is killing people today! Self-interest is a great motivator, but humanitarian considerations should come first.

##### Why can't we give our babies Foxo mutant genes that will give them longevity?
Germ line gene therapy hasn't been perfected yet, but the chances are that it will start to be used pretty soon for the elimination of certain congenital diseases, and once that starts I expect the floodgates will indeed open. But for longevity, no single genetic change will have much effect. Mutations  in FoxO and related genes have much weaker longevity effects in longer-lived species than in shorter-lived ones, basically because the evolutionary pressure to adapt to famines of a given length varies with the frequency of those famines and long famines are rarer than short ones. (See my 2005 paper in Gerontology for details.) I estimate that the most we could get from any such manipulation is a couple of years.

##### What would happen if the 10 richest people in the world each put half of their money towards negligible senescence research?
One thing that never ceases to bewilder me is the frequency with which people raise the same old fears about problems that would be created by solving today's biggest problem, and do so without betraying the faintest suspicion that anyone might have thought about such issues before. It's  breathtaking.

But returning to the original question: actually I think Tony has said pretty much everything I would want to say, in his detailed and excellent response. Many thanks Tony. It's not clear that $200 billion would be appreciably more effective than #2 billion in accelerating the research currently being done - I think $2 billion would suffice to cover pretty much all the bases and leave the sheer difficulty of the science as the rate-limiter - but for sure the subsequent phase, when this work moves from the lab to the clinic, will need very large investment (building new infrastructure, training more medics, etc), and the sooner that investment is forthcoming the more effective it will be in accelerating that phase and bringing agelessness to the masses.

##### Why is it important to understand and study the ageing process?
I agree with the other answers, and I would add this: not only all medicine but all technology consists of going against our evolved state, and I suspect you are generally in favour of the wheel, cell phones, etc, as well as vaccines etc. Aren't you shocked, now we've said these things, at your own bizarre idiocy in having asked the question (even to yourself)? I'll tell you what is shocking to me - that so many people think like your question.

##### I am working on a second book regarding comparative gerontology. Which books do you recommend for my research?
I agree with Marios (for once :-)). Finch's book is 25 years old this year, but does not obviously have a worthy successor.

##### If I am 30 now, what is the possibility that I could live to be 120, with the assumption that medical technology will progress enough in the next 50 years to allow this?  What technology is expected to prolong life in the future?
Well, that's kinda a tautological question - I mean, as of now the main uncertainty is precisely how fast the technology will progress. I could interpret your question as "what is my chance of living to the year 2065 without any such progress, in good enough health to be able to benefit from therapies that arrive at that time?" - to which the answer is probably about 50%, depending obviously on your family history, lifestyle etc. Or I could interpret it as "what is my chance of living until 2105 assuming I benefit from these therapies in 2065 at the age of 80?", to which my answer is probably in excess of 99%, given the progress that will also almost certainly have been made by then in reducing other risks of death.

##### In 2014, what would have been the expected lifespan of someone who did everything in their power, on an individual level, to not die?
The question is kinda backwards, isn't it? If someone is alive at the start of 2014 and does everything they can (within reason) not to die any time soon, they will maximise their chance of making it into 2015. Also, clearly since scientific knowledge is increasing, no one who dies at an advanced age in 2014 could have acted perfectly all their lives with respect to 2014 scientific knowledge. Why do you even care about the question in the form you posed it?

###### Comments
- Mati Roy: Another (and probably clearer) way to ask it would be: for someone who is 18 years old today and has always done and will always do everything in their power to survive, how long could s/he expect to live given our current technologies and knowledge (supposing it stays the same in the future; even if I know it won't). The reason is that I want to remove the speculations about the future from the answers. I will add the speculations myself (with the help of other sources; including your answers to other questions on Quora). I'd like to know how long I could expect to live if I was VERY careful given that current knowledge and technologies stayed the same. This would help me to plan for my future, for my life. This would also help me determine for whom this kind of effort is worth it. For example, if doing everything in one's power only increases one's life expectancy of X years, than I might not recommend it to Y type of people.
  
  So I'm still interested in knowing your answer to the original question. I don't think it's "kinda backwards".
  
  Thank you.
- Aubrey: OK, that's a much less "backwards" question since it fixes the date of birth (to 1997) rather than the date of death. I'd estimate 90-95.

  Also, your motivation for the question (this new one!) is good but not perfect. People absolutely need to know that their own actions, in the near term, will  impact the probability distribution of their and others' experience of aging in the distant future. But in practice, if you think about the maths, it's easy to see that the impact a single person (even someone as influential in the field as me) can have on the distant future of a single person (themselves or any other single person) is small to infinitesimal, because the range of uncertainty of when they will die in the absence of progress and the range of uncertainty of how rapidly the science will progress both greatly exceed the difference to those numbers that one person can realistically make. Therefore, the thing to get people to focus on is not their own prospects but the humanitarian argument, for which the maths is very different. If one decides tha everyone matters, not just oneself or one's loved ones, then one just needs to remember that every single DAY that one brings forward the defeat of aging is over 100,000 lives saved (not to mention all the associated alleviation of suffering). THAT is what gets me out of bed in the morning.
- Mati Roy: Why does fixing the date of birth matters if we consider 2014 knowledge and technologies? Oh, maybe I should have added with 2014 air pollution, and things like that. Thanks for your estimate!
- Aubrey: You guessed it. The main factor is changes in prosperity, leading to changes in early-life nutrition.

##### What is Google Calico doing this long?
They have a near-term strategy and a long-term one. All the press has been centred on the near-term one - the Abbvie deal etc. It's no surprise that they are not talking much about the long-term one, since it's, you know, long-term. However, they now have an actual in-house lab and they hired quite a few people in the past couple of months. I think they'll make a big contribution eventually.

##### Biotechnology: How hard would it be to artificially grow a body that can be used for a human head transplant?
Extremely hard, but most of all, extremely hard to control. If you want a new body, you want it to have the characteristics you choose, and that'd require a way to guide the growth. All in all my money is on printing it rather than growing it. But that's extremely hard too, don't get me wrong!

##### Would we effectively cure aging in most persons if we could: 1) prevent cancer 2) cure heart disease 3) cure neurodegenerative disease and 4) continue vigorous exercise regimens into old age?
You're asking the question the wrong way around. The correct question is "could we effectively cure 1) cancer 2) heart disease 3) neurodegenerative diseases without curing aging?" And the answer to that question is no. It is incorrect to think of any of the diseases of old age as separate, or even separable, from each other: they are all facets of the same network of accumulating damage.

##### Could all the millions of funding poured into Alzheimer's research each year all technically count as aging research relevant for SENS?
No, no more than any geriatric medicine research can. The only subset of Alzheimer's research that does count is the stuff that is focused on damage repair: vaccines and drugs to remove amyloid or tau, stem cell therapies to replace or rejuvenate lost or atrophied neurons, basically that's all. So a reasonable amount, but still a small minority as compared to all the work that is centred on slowing the accumulation of such damage or on treating the pathology itself.

##### Can CRISPR be used to repair genes damaged by aging?
CRISPR has the huge asset of being (in its most recent form) apparently very, very fastidious in its site-specificity. This means (in principle, anyway) that the titre of any vector delivering it can be very high without introducing safety concerns.

However, the problem with repairing somatic mutations is that there are different mutations in different cells. Even if there is just one target gene that we want to repair - let's say p53 - we may have a wide variety of different mutations in it in different cells, including deletions of a large region containing it.

Therefore, I'd say that the only practical way to do this would be to replace rather than repair, i.e. insert a new copy of the gene in a safe location in the genome. But then of course there is the issue of copy number - it may be bad to have an extra copy in cells that have not acquired a mutation in their endogenous copies.

Luckily, though, somatic mutations probably don't contribute much to the rate of aging other than in respect of cancer, so we may not need to do this.

##### Biochemistry: Why do mitochondrial and cytoplasmic reactive oxygen species have opposing effects on lifespan?
I have only read the abstract, but I wouldn't read too much into it. The big problem with C. elegans as a model in biogerontology is that it is just too easy to increase its lifespan - there are literally hundreds of genes whose inactivation does that, including plenty whose inactivation has the reverse effect in other species. In this case there are lots of possible explanations, because clk-1 worms have a defect in their ability to synthesise coenzyme Q, a molecule with an essential role in oxidative phosphorylation but also elsewhere.

##### Are the cells of trees able to live for hundreds (or thousands) of years without suffering significant protein/lipid/DNA damage? If so, how?
It is often said that all living cells even in the longest-lived trees divide at least once every 30 years (with, as Steve notes, very widespread rejuvenating consequences). I don't know the (probably very old) primary literature underlying that number, though. Other than that, all I would add to Steve's answer is that strictly the problem is not that the brain heart etc are made of postmitotic cells, because postmitotic cells can perfectly well die and be replaced from precursor (stem) cells. This is an important distinction, because it allows for the possibility of cell turnover (albeit only very slow, at least in the cerebral cortex, in order that the new neurons can integrate into the network and "learn" from the old ones and thus preserve memory). The essential problem, therefore, is that not only do we have a brain, we have a constant body size (hence brain size) in adulthood. That has given evolution the unfortunate (for us) option of just letting adult neurogenesis degenerate into oblivion in nearly all brain regions, and keeping the body going long enough for reproduction just by incrementally improving (though never to perfection) the arsenal of intracellular maintenance processes, so that most neurons survive as long as the individual needs to. Species with a brain but with continued growth in adulthood, by contrast, need to maintain adult neurogenesis for growth, so they can afford to let neurons die relatively frequently and compensate for that by just doing a bit more neurogenesis than the growth requires. That's the theory, anyway; I am however unaware of any detailed study of cortical neuron longevity in continuous-growth vertebrates.

##### What are the best books (textbooks or others) on aging; principles behind aging; cellular, molecular, physical and chemical, and genetical bases of aging; and every process behind aging, including current research and future approaches?
What Lucas said :-) Thanks for the support Lucas!

##### Could we extend lifespan by growing headless human bodies, and then using those bodies for human head transplants?
The more direct approach would be to 3D-print the body, rather than grow it - growing it accurately would probably be much slower and harder to control. Also, hooking it up to the old head isn't as tricky as all that, when we bear in mind the ability to stimulate nerve growth with stem cells and the plasticity with which the brain can use whatever wiring it has to get what it expects from the body (the example of inverting spectacles is the best known). But unfortunately, the head ages just like the rest of the body, so really the only benefit would be that it would be getting a youthful blood stream. That's not to be sneezed at, bearing in mind what we know about the benefits of heterochronic parabiosis, but it's certain that we will be able to rejuvenate the blood stream by much simpler means well before we can 3D-print whole bodies. So... we'd better just figure out how to rejuvenate the head too...

##### What is a day like in Aubrey de Grey's life?
Not enough sleep!

##### Are there any online journal/reading clubs for the biology of aging?
I don't know of any, but I think highly of journal clubs generally - i.e., regular meetings at which scientists critique a particular paper and learn both what it reported and how to do their own work. It would be great to have an online counterpart of some kind. Well volunteered! :-)

##### Do many biochemical reactions lose their specificity in an aging organism? Could this be a cause of aging?
I think the hypothesis is not that reactions lose specificity but that they go more slowly. The abstract has not persuaded me to take the time to read the full text.

##### Can a cure for lysosomal storage disorders also help with a cure for aging?
Absolutely! - one of the seven SENS stands is "intracellular waste products", which are mostly lysosomal, and our approach to combating them is to get enzymes into the lysosome that can break the waste down, which is exactly what treatments for LSDs typically do. The enxymes will be different but the general approach is the same.

##### Could an independent lab like the Perlstein Lab exist for aging research?
I don't think you mean "independent lab" - that article discusses a $25k crowdfunding campaign, which is going towards work at a lab at Princeton where the guy is already working. Established labs can do meaningful work with $25k (albeit not very much of it, as the article stresses). $25k doesn't go nearly so far if one needs to build the necessary infrastructure too.

##### How is microfluidics used in aging research?
I don't think microfluidics has any specific application to aging research, but perhaps that's the wrong question. Aging research is a specific discipline in name only - since aging affects the body at every level of organisation, both understanding it better and combating it more effectively will inevitably lean on pretty much all the technological tricks that are developed for biological applications generally.

##### Are high cholesterol levels ever bad in invertebrates like C. elegans and Drosophila?
I'm not aware of any really definitive work on that question. Intuitively I would guess that the impact of cholesterol level will be less in poikilotherms generally than in homeotherms, because there will be less tendency for it to be oxidised, but that is speculation - there may be other ways in which it could be harmful.

##### If a person gets an organ transplant, does the transplanted organ age at the same rate as the donor, or does it's age "catch up" to the new host?
The answer depends (unsurprisingly!) on what you mean by "biological age". Some measures, such as telomere length, won't be expected to converge to that of the new host body. Others, such as stem cell function, probably will, based on what we see in heterochronic parabiosis for example.

##### How can lipid damage be repaired?
Well, "lipid damage" can mean many things. Accumulation of peroxides (etc) in membranes is repaired naturally by phospholipases and such like. Oxidised lipoprotein particles are engulfed by macrophages. Etc. So really this is mostly a non-issue: like free radicals, oxidised lipids are not "damage" in the SENS sense but rather intermediates, that can inflict damage on longer-lived molecules elsewhere (typically by being converted into free radicals by reduced transition metals). The main way in which lipids can be damage in their own right is in the case of lipid-rich indigestable garbage, such as lipofuscin, which can be repaired by introducing non-human enzymes that can degrade it.

##### Can one use antibodies to clear out aging-related crosslinks (like glucosepane)?
Since these crosslinks consist of chemical bonds joining structural proteins that we don't want to destroy (constituents of the extracellular matrix), regular antibodies don't seem applicable. However, as it happens, we are indeed looking at this, because one of our other projects is focused on the use of a very unusual type of antibody called a "catabody" that not only binds to its antigen but actually chops it up. We haven't started exploring this yet but it's definitely on our list.

##### Can one engineer bacteria to break down aging-related crosslinks (like glucosepane)?
We've put quite a bit of thought into that over the years, but it's really tricky. What you're really asking is, can we find bacteria that already have the ability to break it down and then transfer that ability to human cells? The transfer should be doable, but the thing is that crosslinks do not themselves serve as nutrients - the bacteria can break down the things that are linked. So there is no selection to develop the enzymes to break the links.

##### How many years will it be before we see a cure for Alzheimer's?
We're still pretty far. One aspect of Alzheimer's, the accumulation amyloid in senile plaques, is basically solved with immune therapy, but on its own that doesn't deliver much benefit. We also need to remove neurofibrillary tangles and replace lost neurons. Approaches to both of those are in development but have a long way to go.

##### Is it easier to cure aging in C. elegans or in mice?
Depends on your definition. If we define "cure aging" as "achieve longevity escape velocity", i.e. repair the damage of aging as fast as it's occurring so that lifespan becomes indefinite, I very much doubt that it will ever be done in either species. It's easiest in the naturally longest-lived species, because in a long-lived species we buy more time by less-than-perfect repair than we do in a short-lived one. If we define "cure aging" as "extend lifespan a lot by doing reasonably comprehensive repair" then it is easier in mice than in worms, mostly because one necessary type of that repair, stem-cell-based repair, is far easier. If we define "cure aging" as "extend lifespan a lot by whatever means", then clearly it's easier in worms - so easy, in fact, that I doubt that we have much to learn about mammals from most of the ways in which it is possible in worms.

##### Can transporting fresh mitochondria into each cell (through cell mitochondrial donation) be an alternative to repairing mtDNA damage in MitoSENS?
Short answer: probably not, because it's too hard to deliver mitochondria to enough cells in vivo. There's also the problem of clonal expansion of mutant mtDNA, which means that the new mitochondria will be outcompeted, but in theory that can be prevented by coadministering an agent that removes the endogenous mtDNA (ideally only the mutant mtDNA, but that's tricky when there are lots of different mutations) and doesn't affect the new stuff. Mito-targeted restriction enzymes are the obvious approach and have been validated already. But again, that's not much good unless you can deliver a lot of mitochondria throughout the body, which is a mighty tall order.

##### Is being angry and unhappy literally reducing your life expectancy?
There is a variety of evidence that stress hormones like cortisol can cause accelerated accumulation of various types of the damage that drives aging, so yes, in general stress is bad - plus, when you're angry and unhappy you are probably at elevated risk of doing something dumb that kills you at once. But aside from that, the impact is probably rather small.

##### How much does shortening of telomeres contribute to aging?
There are whole books, never mind journal articles, discussing this, so I'll just attempt a one-paragraph summary. One thing we can say for sure is that shortening of telomeres is not THE cause of aging, because animals that are engineered to have no such shortening anywhere in their bodies still age (as do animals that naturally have hardly any). Whether shortening of telomeres contributes at all to aging is a harder question, and the balance of evidence in humans is that yes it probably does, but maybe only in the immune system - though, the immune system interacts with the rest of the body in so many ways that that might be enough to have quite wide-ranging effects. But when considering all of this we must also remember that the body has the capacity to avoid telomere shortening whenever and wherever it likes, by making telomerase, and most people think that the reason it generally doesn't is because not making telomerase provides a powerful defence against cancer. Even this is controversial, though, because there are some ways in which short telomeres make certain stages in the progression of cancer more likely. What does this all mean for therapy? Basically it means we need to hedge our bets: develop better and better ways to keep telomeres short and also to keep them long, depending on the circumstance. See the page on cancer at SRF Home | SENS Research Foundation for more, as well as Chapter 12 of my book.

##### Is it possible to form a Manhattan Project/Paypal Mafia/Bell Labs "Young Turks" just for aging?
Well, that's been the idea since 2000. At the small invitation-only meeting where I conceived of SENS, which was held in Manhattan Beach, we were saying exactly that, and George Roth coined the name "Manhattan Beach Project", which is still being used in some circles. Arguably, the attraction of young minds to this problem has been my most significant contribution since then. And as for billionaires, well, I'm sure you know what Peter Thiel has been doing for us since 2006 and how Calico are funded now. It's all happening; the priority is, as ever, just to make it happen faster.

##### What are the factors limiting human life extension?
Rebecca is correct that there is still a huge amount we don't know about aging - which is no surprise, since there's a huge amount that we don't know about biology in general. (Cancers usually have unusually short telomeres, though - problem is they are able to relengthen them just about fast enough to compensate for the shortening caused by cell division.) But our ignorance is not the main barrier right now, because for over a decade we have had a pretty clear idea of how to sidestep that ignorance, i.e. to use what little we do know/understand as the basis for a panel of damage repair therapies that should be able to keep the ill-health of old age at bay.  (See SRF Home | SENS Research Foundation for details.) Thus, the main barrier is that society is still profoundly misguided regarding the whole idea of medicine against aging and doesn't fund it enough. But that's starting to change...

##### What does Aubrey de Grey think of nanotechnology and nanomedicine?
That's a very broad question - so broad that I don't know what you actually want to know. To answer my best guess at that: I think that non-biological solutions to medical problems will continue to become more influential, and that that progress will be driven in large part by miniaturisation (of which nanotechnology, in the Drexlerian sense of molecular manufacturing, is the ultimate extreme), but that the contribution of such technology will not expand rapidly enough to make it the shortest route to longevity escape velocity - we will get there mainly by good old-fashioned wet medicine.

##### Would reaching the technological singularity increase our chances of reaching longevity escape velocity?
Undoubtedly, the more powerful our computational tools (so long as they remain "friendly"), the faster we will develop new medicine, including the rejuvenation biotechnology that will get us to LEV. However, I don't think the technological signularity is a prerequisite: we will get to LEV eventually by just plugging away with our existing intelligence.

##### Is Peter Thiel actually accelerating his rate of aging by ingesting extra human growth hormone?
It's impossible to say. There is abundant evidence from laboratory animals (and now, as you cited, also from human populations) that you'll live longer if you have low GH/IGF-1 (or a low sensitivity to it, e.g. a broken GH receptor gene) **throughout your life**, but the huge thing that such work does not tell us is during which segment of life (if any) this effect occurs. It's perfectly possible, and indeed plausible, that GH etc is bad for you early in life (prenatally and in childhood) in ways that stay with you for the rest of your life, and actively good for you late in life by combating the degenerative aspects of aging. It's a scandal that virtually no direct testing of this kind of hypothesis (using drug-inducible GH transgenic mice, for example) has been performed.

With that said, though, I do think Peter is going out on a limb by taking GH at such a young age. In early middle age the pathologies that GH may resist are still some way off, while the risk of cancer (which he acknowledges, though I stress it is still unclear) will be cumulative, i.e. greater the longer one takes GH. I view cancer as the hardest aspect of aging to fix, so I'm not so optimistic on cancer as Peter is quoted here.

##### Is it beneficial for anyone to track their blood sugar?
Yes, but arguably more important yet is to track your insulin from year to year. Rising insulin levels are a far earlier sign on future diabetes than poor glycemic control, and the sooner you respond to such signs by changing your diet and/or lifestyle, the more benefit you'll get.

##### Where will aging research be in 2020?
That depends on all of us. The pieces are in place to make greatly accelerated progress, but that progress is being slowed, by at least a factor of three in my view, by shortage of funding.

##### What advice would you give a biotech undergrad (intending to end up with a PhD) looking to help make breakthroughs in aging research one day?
There's no simple answer, basically because there's no single thing that should be called "aging research". Since aging affects the body at every level of organisation, it is and alway will be the case that progress against aging relies on an exceptional degree of cross-disciplinary expertise and collaboration. The people who make the most difference in aging research are those who have a broad enough perspective to be able to join the dots. So, don't specialise too much.

##### Can a 42 year old living today expect to live long enough for science to come up with life extension possibilities?
Maybe. Unfortunately, the uncertainty about the timeframes is greater than the timeframes themselves -  I'd say there's a 50% chance of hitting longevity escape velocity in 20-25 years, but at least a 10% chance of not hitting it for 100 years. And even that is without factoring in the uncertainty of whether funding will be enough to let the difficulty of the science be rate-limiting. So my approach, and my recommendation, is not to focus on yourself or your loved ones, but on humanity as a whole. Every year that we reduce the time before the achievement of LEV is about 40 million lives saved, whether it's from 25 years to 24 or from 95 to 94. Does it really matter which lives? Let's just do our best.

##### How helpful will the new Allen Institute for Cell Science be for aging research?
No idea. From what I can tell, it'll be a discovery-centric basic science venture, not a goal-directed effort to use what we already know. Thus, the benefit to aging research depends on whom they hire, and then on the vagaries of what those people discover

##### What is the most low-hanging fruit in aging research?
The answer depends, of course, on how narrowly one defines a cause: for example in SENS we talk about seven **categories** of damage, but within each category we can enumerate many individual types of damage within specific tissues etc. If we go with the seven categories, probably the one we call "intracellular waste products" would be first because it drives the #1 killer in the Western world, atherosclerosis. However, even then we would only expect a few years. To get more than about 15 years we'd definitely need to have at least reasonably effective repair of all seven categories (the sole potential exception being mitochondrial mutations because we don't yet know for sure what pathologies they drive and how powerfully).

##### What would you think is the date of birth of the person who will be the first to live to 150?
Progress in the world record lifespan has halted since 1997, actually - that's when Jeanne Calment died at 122. The oldest living person has never been over 119 since then, and not over 116 since 1999. The reason is not understood in detail, but a basic part of it is that the drivers of the prior few decades' increase were things like better prenatal nutrition and reduction in smoking, which have begun to hit diminishing returns, just as the defeat of the major infectious diseases did before that. But the third era of life extension, which will be driven by regenerative medicine, will almost certainly take off some time this century and maybe within the next couple of decades - and it will benefit people who are already getting on. In particular, it will benefit people who are already 85 or 90 and who were always going to last to 110 or 115. So the first 150yo could indeed have been born in the 1950s.

##### What do people in biology/aging think of the João Pedro de Magalhães paper "The scientific quest for lasting youth: prospects for curing aging."?
Since I accepted it for publication I evidently think it has some merit :-)

However, of course I believe JP is somewhat overpessimistic with regard to the extent to which we really need to understand aging in order to address it medically. But where we agree is that technological progress in biology is so rapid at present that problems which very recently seemed implausibly complex are now becoming tractable.

##### How will artificial superintelligence/artificial general intelligence affect aging research?
Since both the development of superhuman AI and the defeat of aging are extremely hard problems, we can't tell which will be achieved first - but as many people have noted over the years, any important problems that have not yet been solved once we create superhuman AI will probably be solved much faster as a result of it.

##### What things would you do if you could stay young for 100, 1000 or more years (given that you remained as wise as you're now)?
I personally don't think in terms of really long-term goals - I prefer to focus on present-day problems. Of course the fact that a problem will arise in the future if nothing is done to pre-empt it counts as a present-day problem, hence my current focus!

##### What is the truth about the reverse-ageing molecule NMN recently successfully tested in rats?
See this analysis by my awesome colleague Michael Rae:

http://www.sens.org/sites/srf.or...

##### What personal and social issues do you see arising from the longevity/anti-aging agenda? Do the costs outweigh the benefits to individuals and societies?
Rather than enumerate the issues that people typically raise, which most people here have heard a million times before, I think it is more useful to describe how one can decide whether the issue motivates any hesitation or lack of effort to hasten the medical control of aging. You just need to ask yourself three questions:

1) Is it plausible that the unpalatable scenario in question will actually happen? For example, if you're worried about overpopulation arising from a sharply reduced death rate, you need to make sensible estimates of how rapidly the population will grow, and of how rapidly the advance of other technologies (such as renewable energy) will increase the planet's carrying capacity. It's curious how rarely people actually do that.

2) Even if the scenario did happen, is it plausible that the costs would outweigh the benefits? There's a tendency today to underestimate the magnitude of the aging problem, largely because people incorrectly view "aging itself" as somehow distinct from the diseases of old age. If you don't make that mistake, and you classify all deaths from age-related disease as deaths from aging, and all suffering preceding those deaths that those diseases cause as suffering caused by aging, it's pretty hard to escape the conclusion that aging is the world's most serious problem and that no new problem created by solving it could conceivably be as big.

3) Even if the costs did outweigh the benefits as we see them, do we have the right to make that choice? The point here is that if we're so concerned about the undesirable side-effects of defeating aging that we don't get on and do it, we'll be denying humanity of the future the chance to decide differently: we'll be condemning them to the same decrepitude and death that we have today, and they may not be very happy about that. Whereas, if we develop these medicines, our descendents will have the option to decide whether and how to use them. I claim that that makes it our unequivocal moral obligation to defeat aging as soon as we can, whatever our doubts.

##### What is the current state of research to "cure" death and prolong life?
Check SRF Home | SENS Research Foundation and Calico and you'll find all you need to know.

##### What is the most possible way to make people live to 200 years or more?
Not currently, because processes that are essential to life (such as breathing) unavoidably inflict damage on the body that accumulates throughout life, and there's only so much of that damage that the body can tolerate. But in the future, when medicines exist that can periodically repair that damage and thereby keep its abundance down to harmless levels, this limit will be removed.

##### Why does 2-deoxy-D-glucose shorten lifespan in rodents, while increasing lifespan in C. elegans?
I don't think the specific answer is known, but it is an example of a very general phenomenon: scads of interventions (mostly genetic) have been shown to extend C. elegans longevity even though they are very bad for all other animals tested. This is the main reason why I suspect that C. elegans has largely had its day as a useful tool in biomedical gerontology. It may be that we are just very bad at keeping normal worms happy - maybe we're feeding them the wrong type of bacteria, for instance - and that once we develop better husbandry methods they will live a lot longer and these interventions will be life-shortening just as in other species. But that's speculation.

##### Will SENS cause male sterility?
By default, yes it will, because spermatogenesis continues throughout life (unlike oogenesis) and requires telomerase expression in stem cells. But if desired, those stem cells can be repopulated periodically with new ones that start out with long telomeres, just as SENS already proposes for the blood, the gut lining and the epidermis.

##### How does someone apply to the SENS Research Foundation for grant money?
http://www.sens.org/research/grant-submission-process

##### Who is the world's oldest person?
A reasonably up-to-date list of everyone in the world who is validated as being at least 110 is maintained here:

Table E as of August 12, 2014

with the oldest person at the top - currently Misao Okawa, born   Mar. 5, 1898.

##### How can insoluble polyglucosan bodies be cleared from the cell?
Too early to say. The most important thing that (AFAIK) is not yet clear is whether these aggregates are in a state of dynamic equilibrium between creation and elimination, whose equilibrium point shifts with age as a (possibly even adaptive) result of other aspects of aging, or whether they are truly just accumulating with no mechanism for elimination.

##### Why do Japanese people live for so long?
That's still an open question; both diet and genetics probably play a substantial role. However, the most important thing to remember is that in a practical sense they don't! The difference in life expectancy at birth between Japan and the USA, which is something like 40th in the league table of longevity, is only about four years. So we won't be doing much to our chances by just emulating the Japanese: we need new medicine.

##### Where is Aubrey de Grey in 2014?
Short answer: mostly in California but quite a lot in the UK. Long answer: check SRF Home | SENS Research Foundation for event schedule.

##### What is the evolutionary mechanism behind negligible senescence?
Short answer: either it is the result of a lack of separation between germline and soma, such that the evolutionary neglect would also affect the next generation which of course it can't be allowed to do, or else it is non-zero but too slow to have been statistically detectable with the available sample size. Long answer: I'm writing a detailed paper on why aging is not programmed which will appear in early 2015, so watch this space.

##### What is Aubrey de Grey's exercise regimen?
Very much as with my diet, I just seem to be built luckily - I get away with doing very little exercise (not even as much cycling or punting as in the past). As with diet, I recommend that you do what works for you, rather than what works for me.

##### How could a med student best prepare for a career in anti-aging medicine?
There will be two really profound changes to medical practice in the wake of the development of truly effective anti-aging medicine. First there will be a far greater focus than today on prevention, i.e. on treating people who are not yet exhibiting symptoms, and second there will need to be much more emphasis on combination therapies. Both these changes will be hard for medics to embrace, for both technical and doctor/patient reasons. If medical students today are ready for those changes, then 20 years from now when these therapies arrive they will be delivered far more effectively. So. focus on that.

##### What's the difference between bio-engineering and bio-medical engineering?
The obvious: bioengineering doesn't need to be medical. Cleaning up pollutants with bacteria that can digest them (termed bioremediation) is an example that certainly counts as bioengineering but not biomedical engineering.

##### Do naked mole rats suffer any downsides (senescence, apoptosis) from massive p53/p16 expression?
I'm not aware of any major discoveries on that point since the very thorough review you link to came out. The message seems to be in line with what we see in long-lived mammals generally: conserved mechanisms of damage resistance and repair are retained but refined in selectivity and sensitivity, so as to get the best of both worlds in terms of the inevitable trade-offs. I'd expect that we will in due course discover that those trade-offs still exist in NMRs, but in subtler forms than in mice.

##### Could Metformin become the first life-extension drug for healthy people anytime soon?
All we can really say at this point is that metformin is probably working as a "CR mimetic" - a drug that tricks the body into thinking it's not getting as much food as it wants, when in fact it's getting plenty. CR mimetics cause the same changes in metabolism that famine does, so they have the potential to extend life as much as famine does. The problem is that famine seems to have a more profound life-extending effect on short-lived species than on longer-lived ones. Thus, it's unclear whether we can expect much from such drugs - but it's certainly worth trying.

##### Could some of the degenerative effects of aging be the result of molecular crowding?
If you mean this:

Macromolecular crowding

then maybe yes, but it's also vital to remember that the cell is exactly as crowded as it wants to be, i.e. that the changed properties arising form high density of molecules is something that the cell uses to its advantage in all manner of ways. I don't think it will be productive to mess with it.

##### Do mitotic cells age less rapidly than post-mitotic cells because the process of mitosis helps "dilute" out damage like carbonylated proteins and lipofuscin accumulation?
You've got it. The asymmetry you mention does occur, but it works well only when the rate of damage creation per cell division is at an intermediate level, such that symmetric partitioning of the damage would not quite suffice to stop damage accumulating, so that asymmetrical partitioning is the only way to have any descendents at all in the long run. If the rate of damage creation is low enough that symmetric partitioning would suffice, that is generally what is done, since for sure it's better to have two daughters than one.

##### Can lifespan be increased by combining NRF2 activation/Keap1 inhibition with antioxidants?
The problem with this kind of line of attack is that ROS are good for you as well as bad for you: for example H2O2 is an important signalling molecule. That's why the body is so good at compensating for dietary antioxidants by dialling down its in-built antioxidant machinery. It means that the only good way to address the problem of ROS in aging is to go a step downstream in the chain of events and repair the damage they cause.

##### Do very long-lived organisms (like bristlecone pines and quahog clams) suffer from unique types of damage that shorter-lived organisms don't suffer from?
What an excellent question. Racemisation is the one that I would guess first, because it looks like something that (at least in very rigid, extracellular proteins) is so slow that mammals haven't needed to evolve anything to fix it. But in general I would expect that the differences will be subtler. For example, a long-lived species may need to repair a given type of glycation-induced crosslink because it accumulates fast enough to matter for that species, whereas a short-lived species doesn't bother; the result would be that both species suffer aging from glycation, but the specific chemical structure that dominates will be different.

##### How could we design an experiment to test what C. elegans die of?
The first thing to note is that we still aren't particularly good at deciding what humans die of! Largely because of that, I think the best way to ask this question is to side-step it: to step back and ask why/whether we really need to form a view as to what single phenomenon was the proximate cause of death. If a lot of things are going wrong in an organism when they stop moving, does it really matter which one dealt the fatal blow, seeing that others were lining up to do so very soon thereafter? I'd say no.

##### Regarding mitoSENS description in "Ending Aging", in case of duplicated mitochondrial genes, how will the cell decide whether to use the copy from the nucleus or from the mitochondria?
Our current belief is that the cell won't need to make this choice: that there is already a great deal of slop in the stoichiometry of protein synthesis, and this is powerfully compensated for post-translationally, i.e. by the destruction of excess protein, which has a very modest energetic cost. We may be wrong, though, so we're prepared for the possibility that we will need to build in some kind of regulatory apparatus such that the nuclear copies only turn on as and when the mito copies are disabled - but we'll cross that bridge when we come to it.

##### As a 30 year old that cares for his health and exercises in moderation, how old do you think I can get?
Anthony is completely wrong, but maybe not for long. At present, pretty much all actuaries make predictions based on past trends, which is totally hopeless because it ignores future technological (and, lesserly, social) developments that will drive deviation from those trends. Very recently, however, a few experts in this area have bitten that bullet and begun to develop forecasting systems that do work on the basis of future developments, and they are being taken very seriously: really the only big barrier right now is inertia arising from sunk cost, i.e. the astronomical bets that have already been placed based on the extrapolation approach.

##### What kinds of projects is Aubrey de Grey working on in 2014?
Sorry for the slow reply. Rather than enumerate, I refer you to our website SRF Home | SENS Research Foundation and specifically to the research pages, which are pretty up to date. We will also have a new annual report out within the next week or two, which will also be posted there.

##### What is it like to attend the Rejuvenation Biotechnology Conference 2014?
Heh - it's probably not for me to say! But it certainly seems as though everyone is very happy they came. My colleagues at SENS Research Foundation have done a fabulous job putting it together.

##### What can/should a high school student interested in ending aging do?
Two things, mainly:

- Learn enough biology to understand the gaping flaws in the sort of thinking exemplified by the start of Lynn Teatro's answer;

- Learn enough psychology to understand why otherwise perfectly smart people persist in embarrassing themselves so egregiously on this topic.

Then you'll be equipped to do something about it.

##### How can damage to extremely-long lived proteins (like nuclear pore complexes) be repaired?
Many thanks for this extremely important question. I and SENS Research Foundation have been paying close attention to it for many years, because it is indeed possible, in principle, that proteins other than the extracellular matrix (which of course is already a target of SENS) could be recycled so slowly that their damage accumulates. We've had talks at SENS conferences on this, such as from Satoro Goto on histones; we also invited Hetzer when his first report on NPC proteins came out and he initially accepted but then withdrew at the last minute.

So... the short answer is that at present I think there is probably no need to worry. In Hetzer's original work, if you check carefully, there was only one subunit that was both detectably damaged and not detectably turned over. I was actually pretty relieved when his group's more recent work so minimally extended that original report. But to answer your question directly, if there turns out to be any protein to which damage occurs that seems to contribute to the ill-health of old age,  we have the usual options: repair the damage (such as by breaking glycation-induced crosslinks), or stimulate turnover (with antibodies, for example).

##### What are some of the most important papers in aging research?
There is a pretty extensive bibliography at <SRF Home | SENS Research Foundation>.

##### I wish to dedicate my life to anti-aging research. How should I plan my education?
I agree with others' answers here (and I'm amused at Ellen's reticence concerning the achievements of her relative, whom I often cite as one of my real heroes). Indeed the older you get the sicker you're likely to be when you die - but we're in the business of changing that. All I would add is that there's no one generic answer to the original question: it depends what you're good at, what you most enjoy doing, etc. We encourage people to write to us at SRF Home | SENS Research Foundation telling us a bit about themselves and asking this qustion, and we do our best to give specific advice.

##### If I gave the SENS Foundation 1 billion dollars, how would this affect its current timeline?
Thank  you for asking this. Since I was able to (temporarily!) double the  foundation's budget two years ago with the proceeds from my mother's  inheritance, we have moved to the level of working on nearly all the  areas that we feel are dangerously neglected by others. What's next,  mostly, is to elevate these projects from the "entry level" state that  they currently occupy (at most three people per project, often only one  or two) to a level of staffing that will allow the projects to progress  at a rate limited only by the science. Sometimes that means moving from  cell culture to mice, sometimes it means introducing greater  parallelism, sometimes it entails expensive kit - that depends on the  project. But we could certainly spend $50M per year at once, as against  the $4M per year we have today - and I believe that our overall rate of  progress could be trebled thereby. That's a lot of lives being lost  right now. I'd probably spend your $1B at a rate of $100M/year.

##### How much beer does Aubrey de Grey drink per day on average?
Only three or four pints. Also, let me be very clear that I do not recommend that people in general adopt the same lifestyle as me: everyone is different, and the same diet, exercise regimen etc may be great for one person but bad for another, The only general advice is to pay attention to your body. I weigh the same and have the same vitality at 51 that I had at 17, so my best strategy is to stick to what I know, but if and when that ever changes, so will I.

##### If SENS funding remains stable, how many years away are we from robust mouse rejuvenation?
Ivan has it pretty much right. It's probably not quite that bad - it won't stay at 3x, because some of the necessary progress will be made serendipitously for other reasons - but I'd say that at this point the 50% threshold is about 15 years from now if funding remains in the current $4M/year range, as against 6-8 years with $100M/year.

##### Did the late-2000s economic crisis significantly slow down aging research since Aubrey de Grey's publication of "Ending Aging" in 2007?
Oh yes, severely. On the public and commercial funding sides, the effect has been the same as for research and biotech (respectively) in general. Closer to home, I can immediately think of three very wealthy supporters of SENS Research Foundation (or to be more precise Methuselah Foundation, since we had not yet bifurcated it), including one who had for the previous couple of years been our second-largest donor, who have cited crisis-induced belt-tightening as their overriding reason for not donating to us since then. (Yes, they haven't adequately recovered even now.)

##### What are your expectations for Crispr/Cas9?
It's a complete game-changer, in my view. Its ease of use and its versatility are streets ahead of its precursors (ZFNs and TALENs), let alone earlier ideas. Also, in recent months its fidelity (avoidance of off-target effects) has been greatly improved. It does still remain to be seen how well it works as a somatic gene therapy technology, but SENS Research Foundation is working on the basis that it will work well, and we're developing complementary technology to allow high-penetrance insertion of large cargos into a specific site previously created using CRISPR.

##### What has been learned from the failed anti-amyloid antibody trials?
I don't have much to add to the other answers (so I'm really only answering because I've been asked to). The short answer is that we learned very little, because it was already widely believed/established that senile plaques per se are minimally if at all involved in the pathology. All we've definitively learned is that the pathology is dominated by other aspects of the disease - tangles, precursors of tangles and plaques, and/or neuronal loss or atrophy, and that the clearance of plaques doesn't dramatically change that. It could have done, e.g. if clearing plaques had allowed a rapid acceleration in the clearing/aggregation of amyloid beta oligomers, and if those oligomers are the main toxin in AD - but those were always very big ifs. So for now, all that can be said is that it's a good thing that we now have technology for clearing plaques in our back pocket as something to co-administer with yet-to-be-developed therapies to eliminate plaques, replace or reinvigorate neurons, etc. We're going to have to get used to the fact that complex diseases, which means most diseases of old age, will only yield to complex, multi-component therapies.

##### If we could print all major organs of the human body, how many years would that alone add to average life expectancy?
Probably very little. The brain would presumably still age as now, and so would our muscles, bone marrow etc, which would send us downhill pretty fast.

##### In a 2005 TED talk, Aubrey de Grey said that we can achieve robust mouse rejuvenation in 10 years. How is that timeline looking like right now?
Yes, I said that - in fact, I think I first said it in 2004. However, I qualified it (well, I usually did - I hope I did in that talk!) by "with adequate funding", which I was already placing at $100M/year. In fact, our average budget in the intervening decade has been around $2M/year (it's currently about $4M). We've used it well, and I'm pleased to say that in my estimation we've progressed roughly 1/3 as fast as I hoped we would, such that we are now about three years closer to RMR than we were then. But it's still the case that we're going only 1/3 as fast as we could if we had 25x more funding. Even 5x more funding would probably double our rate of progress.

Of course there is the additional qualification, which I also perennially stress, that these timeframe predictions are only for a 50% chance of achieving the relevant milestone, rather than certainty - but you knew that.

##### What would happen if an enzyme had lots of disulfide bonds so it could still work at temperatures as high as 700 C ? Could we be engineered to survive on planets deemed too hot for human survival?
That's a non-starter. Enzyme activity relies not only on the enzyme being the right shape to bind its substrates, but also on its having the right propensity to alter its shape following that binding, so as to lower the activation energy of the reaction it catalyses. That change of shape ("conformation" is the technical term) would be hindered by anything that hinders the change of shape resulting from high temperature, whether it be disulphide bonds or anything else. Of course this is not an inescapeable mutual exclusivity, or else we wouldn't have thermophilic bacteria - but the only way out of it is to evolve a whole bunch of individually deleterious (and un-designable) changes that work together to get the best of both worlds.

##### What is the difference between the Methuselah Foundation and SENS Research Foundation?
In terms of overall mission, no difference whatever. The difference is purely in terms of how we go about it: MF  mainly focus on promotion and advocacy, via prizes especially, whereas SRF mainly focus on specific research projects. We decided back in 2009 that these two approaches would be more effectively pursued in separate organisations, not least for messaging reasons, and we definitely feel that that has worked.

##### Alzheimer's Disease: Is eliminating beta amyloid an easier problem than eliminating hyperphosphorylated tau?
Yes, far easier (according to current evidence). Since 1999, it has been apparent that plaques can be eliminated by vaccination, i.e. by stimulating the immune system to engulf them. This has since been demonstrated in clinical trials. Tangles, on the other hand, are already inside the cell and should thus be destroyed by whatever machinery the cell has at its disposal - but they aren't. Thus, either we need to give the cell new catabolic tools to destroy tangles (analogous to what SENS Research Foundation is exploring for the equivalent targets in atherosclerosis and macular degeneration), or else we need to find and eliminate whatever other toxin may be preventing neurons from destroying tangles - which may, actually, be the same stuff as in atherosclerosis, but we're not sure of that yet.

##### Longevity: How important was the recent discovery of the effects of GDF-11?
Fairly important. The stimulation of neurogenesis in brain regions where it already occurs naturally to a certain extent (but declines with age) is not as exciting as if it occurred in regions where there is normally none, but it's still bona fide rejuvenation, and the more demonstrations we have of that, the more people will accept that truly comprehensive rejuvenation is foreseeable.

##### How does Turritopsis dohrnii jellyfish deal with carbonylated proteins, lipofuscin accumulation, and nuclear DNA damage?
I don't know the detailed answer, but the top-level answer, which is all we need to know for biomedical purposes, is that it does so by not having any tissues that rely for their function on indefinite cellular longevity. In other words, all cells can and do divide and thereby dilute or select away any damage.

##### If bacteria can be effectively "immortal", then couldn't mitochondria also be effectively "immortal"?
First, the asymmetric distribution of damage is a trick that  is not universal among single-celled organisms - it is a way to let one cell keep damage low in the case where the rate of damage accumulation is just slightly too fast for cell division to allow both cells to keep damage low, but if the damage is being created slowly enough then symmetric distribution of damage is preferable.

Second, we must distinguish between genetic and non-genetic damage to mitochondria. Non-genetic damage is definitely reduced by anything that accelerates mitochondrial biogenesis, because the damage is transferred more rapidly to the lysosome via autophagy. But genetic damage (mutations) may actually accumulate a little faster, because it mainly occurs via clonal expansion, not by a succession of new mutations.

##### Does 'Big Pharma' experience a conflict of interest when doing SENS-type aging research? What are the consequences?
Certainly SENS has this problem, as does all preventative medicine, But in the long run it won't be a problem. Really the only reason why the medical industry makes its money out of sick people is because the public think that way: they aren't all that keen on submitting themselves to experimental new medicines when they aren't yet sick. So that's what we need to change - public attitudes to the value of preventative medicne - and then the industry will follow the money, one way or another.

##### Who are high-quality estate attorneys, who prepare wills, trusts, medical living wills, etc., who are experienced in incorporating plans for cryonics, including establishment of a trust fund for possible future restoration/resurrection costs and funds for the revived person to deploy?
Start with Rudi Hoffman, who is very easy to find online. He will either be your ma or know whom to send you to.

##### Are Aubrey de Grey's estimations for the advent of SENS changing over the time he makes them?
The short answer is "yes" - but I think it's worth giving some details, because if more people understood what is currently the best way to hasten progress then it would certainly happen sooner. It's been about ten years since I started making predictions about how soon we would achieve (a) the trebling of a middle-aged, naturally long-lived mouse's remaining lifespan - something I called "robust mouse rejuvenation" (RMR) - and (b) the doubling of a typical 60-year-old's remaining lifespan, which I called "robust human rejuvenation" (RHR). It was also around then that I introduced the concept of longevity escape velocity; I claimed then that RHR would almost certainly suffice to achieve LEV, and I still think so. So, back then I said that it would take about ten years to get to RMR and 25 years to get to RHR, each with 50% probability, so long as funding of all the relevant research was adequate. These estimates are/were of course massively speculative, such that (whenever I got the chance) I also clarified, as I still do, that there's at least a 10% chance that we won't achieve RHR for 100 years - but that's fine, a 50% chance is ample motivation. So, what's happened in the past ten years? I think we're about three years closer to RMR, in other words we've slipped by about seven years. We've probably slipped by only a couple of years for RHR, because the fact that the translation of RMR to RHR will be happening later means that it will be able to take greater serendipitous advantage of discoveries made for other reasons. So now, does this mean I was overoptimistic, and what does that imply for the future. The answer is that the only area in which I was overoptimistic was with regard to the ease of securing adequate funding: I think I would indeed have predicted that the funding we've actually had would have resulted in progress being about three times slower, which indeed it has been. The conclusion is clear: the world is spurning the opportunity to make a really big difference to how soon we bring aging under medical control and to save a vast number of lives, probably in the hundreds of millions.

##### Which people in the San Francisco Bay Area do aging research?
There are masses, especially if (as I would recommend) you define "aging research" to include all work that is done for the purpose of, or can be applied to the task of, comprehensively postponing age-related ill-health. Obviously my view is that the organisation doing the most important such research is SENS Research Foundation, SRF Home | SENS Research Foundation - we are based in Mountain View.

##### How would the SENS Research Foundation use a large donation?
Thank you for asking this. Since I was able to (temporarily!) double the foundation's budget two years ago with the proceeds from my mother's inheritance, we have moved to the level of working on nearly all the areas that we feel are dangerously neglected by others. What's next, mostly, is to elevate these projects from the "entry level" state that they currently occupy (at most three people per project, often only one or two) to a level of staffing that will allow the projects to progress at a rate limited only by the science. Sometimes that means moving from cell culture to mice, sometimes it means introducing greater parallelism, sometimes it entails expensive kit - that depends on the project. But we could certainly spend $50M per year at once, as against the $4M per year we have today - and I believe that our overall rate of progress could be trebled thereby. That's a lot of lives being lost right now.

##### How can I get interviewed/recruited for Google Calico?
To the best of my (limited) knowledge, Calico are still taking their own good time with making decisions, including hiring. Just today it was made public that Cynthia Kenyonis quitting UCSF to join them, but she was quoted as follows: "Calico is still sorting out directions and priorities and is not yet in a position to be talking about itself."

##### What does Aubrey de Grey eat?
Nothing special. I'm one of those lucky people who are built well for health and youth: I can eat and drink what I like and nothing happens. I'm not recommending the same strategy to others!

##### Does the slope of telomere erosion decrease with age?
I'm not really sure what you mean by your question, since you posted a graph of the data from an investigation of exactly that. I would say that there are three points to note in this regard:

1) Different studies will give different answers and cannot necessarily be aggregated, since they may study different tissues or use different telomere measurement techniques.

2) The question "Does X change with age?" (where X can be a rate, or for that matter a rate of change of a rate) is really an abbreviation of the question "Is the hypothesis that X does not change with age excluded, to 95% (or your favourite value) confidence, by the available data?". And that is often a rather hard question to answer from a purely statistical perspective, which is why statistics is still a research field. I have absolutely no idea whether the graph you posted is or is not an example of an affirmative answer to the question.

3) There are various known biological phenomena, and doubtless plenty more that are unknown, which make this question not necessarily the most important question in terms of the relevance of telomere shortening to aging, which I'm guessing is why you asked it. For one, telomerase preferentially elongates short telomeres. Another: the telomere length needed to protect against end-to-end chromosome fusions and other bad things is probably a good deal shorter than what is seen in studies like this even in old age. Another: the cellular malfunction caused by critically short telomeres is also caused by critically frequent chromosome breaks, which is believed to be why mouse cells senesce in culture so fast even though they have immense telomeres. And the most important of all: telomere shortening may be good for us (up to a point) as a defence against cancer.

##### Is the decline of fluid intelligence in early adulthood (age 20 to ~35) more the result of actual age-associated "damage" (like oxidative stress/protein carbonylation), or more the result of continued optimization (e.g. synaptic pruning)?
I agree with Selim. It is extremely challenging to separate the neurochemical and sociological influences here.

##### Does exercise increase free radicals in all tissues (including the brain), or does it only increase them in muscle tissue?
Exercise doesn't necessarily increase free radicals anywhere. First of all you need to distinguish between FR production, scavenging, damage inflicted and damage repair; I think you're referring to production. Mitochondria actually make more free radicals when they are idling than when they're making lots of ATP - basically when they are highly charged (in the sense of a capacitor) the charge can leak out more easily. That's a big part of why exercise (in moderation!) is good for you.

##### Is it possible to visit the SENS Research Foundation for fun?
We're happy to receive visitors from time to time, but naturally we have to be quite restrictive about it in order to keep disruption of our research efforts to a minimum. I'll be honest and admit that we give priority to donors... Email me (aubrey@sens.org) if you want to know more.

##### Given SENS work, what would people aged 200 look like?
The biological age of the skin and the external appearance will be the same as that of the inside of the body. So, depending on how frequently and how thoroughly rejuvenation therapies are administered, one could be biologically in one's 20s or in one's 40s - but the inside and the outside should be the same.

##### Does calorie restriction extend life in humans?
My view, as expressed in detail in my 2005 paper in Gerontology, is that CR works less well in long-lived species than short-lived ones because long famines are rarer than short famines and thus there is less selective pressure on long-lived species to evolve/maintain machinery to respond with a given degree of impressiveness to nutrient deprivation. This is in line with virtually all available data.

##### What happens to the protein/lipid damage that the daughter cells of older mothers/fathers accumulate once the daughter cell starts development?
Precisely. Plus, there are all sorts of clever mechanisms in place during gametogenesis and following fertilisation that select out genetic damage, not least to mitochondrial DNA.

##### What are the downsides (if any) of eating too many monounsaturated fatty acids (MUFAs)?
You have it right. I have never encountered so much as a hypothesis for any issue with MUFAs.

##### How important are thermodynamic molecular disruptions in aging?
The example you propose, amino acid racemisation, is probably not relevant to aging in a currently normal lifetime: we have defences against it in free amino acids, and in long-lived proteins it seems to happen too slowly to matter. The accumulation of the various types of molecular and cellular damage that do in all probability contribute to the ill-health of old age can be described as an entropy problem, i.e. a thermodynamic problem, but I'm not sure how useful that is: the 100000-foot summary of how we live as long as we do is that we're really good at exporting entropy, so basically the goal of anti-aging medicine is to improve the comprehensiveness of that export, but I don't think that's a particularly productive way to think about it for the purposes of actually developing such medicine.

However, there is one aspect of the role of entropy in aging that is scandalously overlooked, even by experts, so let me draw attention to it. It is far too often said that the variability in rate of aging between individuals comes from two sources: genetics and environment. However, as was very thoroughly reviewed by Finch and Kirkwood in their excellent book "Chance, Development and Aging" quite some years ago, there is a third contributor, namely simple randomness at the molecular level, i.e. Brownian motion. This plays its role mainly during early life, leading to "cohort effects" in which differences in (to put it simply) how old you are biologically when you're born stay with you throughout life. More recently Tom Johnson's group have provided particularly compelling evidence in worms that this contribution to inter-individual variability is probably greater than either genetics or environment.

##### How can machine learning be used for aging research?
This is a highly apposite question whose answer is entirely unclear at this point, but my money is on machine learning being very useful. There are bound to be contributions from such methods to the whole area of personalised medicine, i.e. the optimisation of therapies to a particular person, but that isn't specific to aging. What may be specific to aging is the identification of connections across disciplines: biogerontology is probably unique in the extent to which it draws on so many other aspects of biology, and I can tell you that the lack of sufficient cross-disciplinary expertise results in a huge amount of useless work being done that could have been avoided if anyone had known all the relevant facts (or if anyone who did know them had been consulted in advance!- but I don't mean to be snarky, because in general it's the former). Machine learning has the potential to give researchers a big leg up in figuring out which experiments to do next.

##### What should a student major in/study if they want to go into the biology of aging?
The best thing to do at undergrad level is a general biology degree. It's a bad idea to get into any particular speciality (biochem, genetics, physiology) at that stage, because aging affects the body at every level of organisation and thus one needs a reasonable grounding in pretty much the whole of biology in order to be useful later on.

##### How is it that we're able to synthesize so many novel psychedelic designer drugs and not able to make (advanced glycation endproduct)-breakers?
Justin has pretty much covered it. Another unfortunate feature of this problem is that the first two reasons he mentions (not many people, really hard problem) are inextricably linked in a catch-22 by the nature of academic and commercial funding, which are both massively biased (for different reasons) against high-risk high-reward work. It is mostly for that reason that SENS Research Foundation exists, so as to direct philanthropic funds to these critical problems.

##### Could one win the Methuselah Foundation mouse prize by combining calorie restriction, IGF1R knockout, AGE breakers, rapamycin, and metformin - all with each other?
I'm certainly in favour of such combination approaches. Obviously I don't know whether they would work until someone tries, and one would not want to include the genetic manipulation if one wanted to go for the Rejuvenation Prize (the big one, which is restricted to late-onset interventions), but I would loe to see more such work. The main disincentive to do combination interventions is that they are viewed as hard to interpret mechanistically, but I don't think much of that argument.

##### Why is there no Methuselah Prize for C. elegans?
We thought hard about that (and similarly for Drosophila) back in the day, but we came to the conclusion that there wasn't much case for it as a way to further the goals we had for the mouse prizes, which were (a) to encourage research that would inform the development of human interventions, and (b) to get the public excited about foreseeable prospects for human interventions. By both measures we felt that one really needs to use a mammal.

##### Can marijuana increase lifespan in mice?
It's as reasonable a theory as there usually is to motivate lifespan studies - but of course most lifespan studies come out negative. I don't know whether it's been tried.

##### What do you think of Human Longevity, Inc.?
It's extremely exciting. I'm not one of those who believe that the ultimate solution to defeating aging lies in personalised medicine - I think we are well on the way to generic treatments that will just work for everyone, which is what SENS Research Foundation works on - but in the nearer term we will certainly benefit from data like this. Perhaps even more important is the involvement of larger-than-life characters at the head of the organisation in the form of Venter and Diamandis: irrespective of what HLI actually work on and how useful it ends up being, there will be a huge and much more immediate impact on the perceived credibility of doing something serious about aging. With Calico coming in too, the task I've so long been engaged in of getting people to believe that this is not a futile quest may truly be nearing its end.

##### Why are higher citrate levels associated with higher all-cause mortality?
There's no stand-out obvious explanation. Since this is (AFAIK) the first time that circulating citrate levels have been correlated with mortality, I think it is probably premature to speculate. Note also that this was a study of near-term mortality, so it mostly gives markers of the body's responses to relatively severe illness, rather than markers of what brought about that illness in the first place.

##### How would society be affected if the average human lifespan was 200 years?
To be honest I don't think it's productive to speculate about matters like this, for two reasons: (1) there are so many unpredictable factors involved that it's purely guesswork, and (2) it's impossible to come up with any remotely realistic scenario that would be unpalatable enough to give reasonable cause for hesitation today in developing therapies to postpone the ill-health of old age, which is the only thing that such predictions are ultimately useful for, even notwithstanding the rather iron-clad moral argument that whatever we may predict we have a duty to give humanity of the future the tools with which to make their own choices. Let's just get on and develop these therapies and quit all this navel-gazing.

##### In terms of investment what do you think is a possible return for a drug or treatment who could extend human life span by 10 years or more?
The fist thing to do is list the quantitative variables that are omitted from your question. One must specify not only how much longer the average beneficiary of the treatment would live, but also (at least) the following:

- how much of the extra life would be healthy and how much unhealthy

- how soon the drug would be expected to become available

- how much it would cost to produce

- how old a beneficiary should be when first receiving the treatment

The last of the above is the one most often forgotten, but it's by far the most important in arriving at any kind of useful answer to your question. It's the main reason why preventative medicine in general (defined as medicine that's designed to be given to people who are not yet exhibiting significantly diminished physical or mental function) comprises such a tiny proportion of the number of approved drugs and treatments (and a slightly less tiny proportion of the overall medical budget only because of a few blockbusters such as statins). Ultimately, even though everyone is well aware of the crushing economic (even leaving aside humanitarian) burden currently imposed by Alzheimer's disease, a drug that can stop you ever getting Alzheimer's disease however long you live is only going to sell if it works on people who are within a few years at most of coming down with it, and ideally on those who already have it. (I use Alzheimer's rather than "aging in general" here only to avoid yet another foray into the tedious issue of whether there is any useful difference between aging and age-related ill-health: there isn't, and if you really still don't know why you're welcome to check me out on youtube or wherever.) If it only works for those who have taken it since childhood, it will constitute an economically unattractive investment (whether viewed at the level of the individual or of society as a whole), because no health benefit will actually be seen until unacceptably many years of pumping money into manufacturing and delivering the treatment have elapsed. Plus, in those years there is always the chance that someone else will develop a treatment that works just as well even when initiated in middle age, in which case the first drug never delivers any benefit at all.

Unfortunately, once someone has Alzheimer's (and, of course, what I'm saying here applies with equal force to any progressive disease of old age), options for treatment are extremely limited because things spiral out of control into totally unmanageable chaos. It's no accident that we've never cured, and rarely even modestly postponed, any age-related disease, despite our prodigious success against most of the diseases that used to be prevalent at all ages.

That's why what we should be aiming for is the sweet spot between prevention and treatment: interventions that treat the precursors of such diseases, rather than the diseases themselves, but that do actually TREAT (yes, reduce) those precursors rather than just impeding their further accumulation. Such therapies will not only prevent the corresponding diseases even in those otherwise on the point of developing them: they wlill also potentiate the currently ineffective treatments for such diseases by eliminating the inexorable rise in abundance of their precursors. See SRF Home | SENS Research Foundation for how I think we can do this.

##### Longevity: Has the total synthesis of glucosepane been published?
Not yet. Patience!

##### Longevity: Would a probe for glucosepane have commercial diagnostic value?
Definitely - very big value. Abundance of glucosepane is probably the single most relevant quantity indicating the contribution of ECM crosslinking to hypertension, which would be a key factor in choosing therapeutic options.

##### How significant are the findings in the December 2013 paper about the effect of "Nuclear-Mitochondrial Communication" on aging?
Short answer is it’s not all that big a deal in biomedical terms. It’s a great discovery in terms of understanding mitochondria, and it provides a new way to rejuvenate mito function, but it doesn’t tell us that rejuvenating mito function in isolation in an otherwise still-old animal is a good idea - and there have for many years been other ways to rejuvenate mito function which did not lead to longer lifespan. But note that that doesn’t mean we can be complacent about mito mutations, one of SENS’s main themes, and stop trying to fix/prevent/obviate them: this study has nothing much to do with mito genes, but rather the function of the huge majority of mitos whose genes are intact.

##### Do people age linearly?
The underlying rate of accumulation of molecular and cellular damage is basically smooth, though somewhat accelerating because damage is also incurred by our damage-repair and damage-preemption systems (making them perform less well as aging progresses). The outward consequences of this damage in terms of declining mental and physical function are more "bursty".

##### What are some potential specific reactions that could break up glucosepane in AGEs?
This is indeed an extremely challenging problem. Glucosepane is a very weird molecule (with a seven-membered ring in it), very different from anything that the body makes on purpose, but still the design of a reagent that will attack it without attacking anything else is not at all easy. But we are funding a really terrific lab to look at the question, so we're optimistic. Also, one feature that applies to this project and also to quite a few other areas of SENS is that the accumulation of glucosepane is so slow that even a really inefficient reaction is all we need to reverse that accumulation, maybe even over a period of years.

##### Are there any conceivable dangers from having far more mitochondria than normal?
There are indeed abundant such dangers. It has been known since the 1970s that mitochondria generate more free radicals when they have a high proton gradient, which happens when they are "underemployed" - when there is lots of carbohydrate or fat around to supply energy and the relevant metabolic intermediates are thus being supplied to the respiratory chain, but when not so much ATP is being used. That's the main reason why Ames and Hagen used lipoic acid: it itself does not increase mitochondrial activity, but it neutralises the free radical elevation caused by the thing that does, namely the other component of their formula, acetyl-L-carnitine.

This is a very complex area of biochemistry, as it turns out, with counterintuitive behaviour in many respects. But the bottom line is that the cell already knows pretty well how to judge how many mitochondria would be too few or too many, so it's hard to see why we should mess with it.

##### Longevity: Did SENS get any good insight into how to clear glucosepane using Innocentive (Breaking Advanced Glycation Endproduct Glucosepane, a Protein Cross-link?  )?
No, it wasn't useful. It was always a real long shot. There's a clear path only in the sense that we need to find drugs or enzymes that cleave it, which is really hard; at this point we're still very much at the preparatory stage of developing tools to determine how much of it there is, etc.

##### How accessible are the AGEs (such as glucosepane) in crosslinked protein fibrils?
First note that the problem of glucosepane (and, possibly, other AGE crosslinks) is not related to the problem of amyloid plaques: plaques just need to be destroyed wholesale, which is a whole different SENS strand than the crosslink problem. The fibrils referred to above are constituents of the extracellular matrix, whose elasticity we need to restore without destroying it.

So: we're considering a range of options here, whose merits will depend on what we find as we move forward with the discovery of agents that cleave glucosepane in easily accessible contexts. One possibility is to use organocatalysts, which are small proteins that work as somewhat non-specific enzymes: basically a compromise between regular enzymes (specific but large) and regular drugs (small but non-specific). We're keeping our options open at present.

##### Is aging linear or does it follow a step function?
I don't know of any study of this kind of phenomenon. It's not particularly counterintuitive, though, because there are various defence/repair mechanisms in the body that are triggered only once their target damage exceeds a certain threshold. One would expect that functional decline driven by those types of damage would then exhibit something like a step function even though the causative damage is accumulating at a smooth rate. The same logic works in the case of damage repair mechanisms that become overwhelmed and suddenly cease to work as well as previously.

##### Why can't we prevent death?
One reason we can't "cure" "death" is the bizarre tendency of so many people to use words like "cure" and "death" so inappropriately, leading to public failure to appreciate the possibility of medical interventions to postpone (maybe indefinitely) age-related, life-threatening ill-health. Why can't we dramatically postpone age-related, life-threatening ill-health yet? Because it's very hard to do, but also because people keep mis-stating the question.

##### What are Aubrey De Grey's thoughts on Google's announcement of Calico, a company aimed to focus on aging and associated diseases?
I expressed my enthusiasm in Time:

Finally, the War on Aging Has Truly Begun | TIME.com

##### Do exercise and restricted calorie diets activate the Heat Shock Protein pathways?
I'm not sure whether this has been studied, but I wouldn't be at all surprised if some heat shock proteins are elevated in primate CR. These proteins are named somewhat misleadingly, because they protect the cell and the body against a wide variety of different stresses, and CR is a form of mild, systemic stress. Whether artificially elevating such proteins would mimic CR is much less clear.

##### How did you overcome the fear of death?
Well, 20 or so years ago when I discovered that most people were doing nothing about it, I decided to switch careers and do as much as I could about it. It's been a highly fulfilling decision so far, and who knows, it might even succeed. More to the point, whether or not I personally benefit from my own efforts spearheading the biomedical defeat of aging, 100,000 other people will for every single day that I bring that milestone forward. That's a pretty effective thought with which to get yourself out of bed in the morning.

##### What are the best ways of reversing AGEs?
Short answer: there is currently no way to reverse the accumulation of AGEs. There are various drugs, including those you mention, that may slow the accumulation, but of course that's not nearly so interesting. One of SENS Research Foundation's main research programs is to find ways to break AGE crosslinks.

##### Biomedical Engineering: How far away are we from personalized nano-medicine?
Short answer: too far away for it to be possible to put a number on it, and that's coming from someone who believes that it's vital for experts to put numbers on things like this even when those numbers have to be extremely speculative. The main barrier to applying molecular manufacturing to medicine (as explored by Freitas) is simply the development of molecular manufacturing at all. While there have been very considerable theoretical advances, it seems we are still a long way from being able to manipulate single atoms (or small numbers of atoms) in the manner described by Drexler, even though it now seems clear that the various reasons put forward by Smalley and others that such manipulation is theoretically impossible are invalid.

##### What are the best arguments in favor of life extension?
The single best argument is not strictly an argument for life extension at all: that life extension is not an end in itself but merely a side-effect of future medicine to maintain totally youthful health irrespective of chronological age. If you're against the idea of people living a very long time in youthful good health, then you're only in favour of medicine for the elderly so long as it doesn't work very well, i.e. you think people over a given chronological age SHOULD become sick and frail so that they'll die soon. Conversely, if you accept that old people are people too and are just as entitled to good health as young adults are, you can't logically also oppose the effort to develop medicine that will keep them in that good health. If you are so scared of what a world without aging would be like (whether because of potential overpopulation, immortal dictators, boredom, whatever) that you genuinely doubt whether the benefits of such medicine would be outweighed by the problems created, then the onus is on you to actually examine those potential problems and consider whether there are plausible ways in which humanity could avoid them, rather than (as is so common) just to uncritically presume that they will "obviously" occur and not be avoidable.

##### Transhumanism: How can I become a transhumanist activist?
The way to become an effective activist in any technical field is to start by gaining a good understanding of the underlying science, and then to read a lot of what other activists and experts are saying to counter the concerns raised by others concerning what a world with the technology in question would be like and think how those arguments might be improved. Far too many advocates of radical new technologies do more harm than good for their cause by offering oversimplistic arguments against common concerns.

##### Is it true that insulin makes you age faster or is it just more dieting mumbo jumbo?
In humans, there is certainly a correlation between high insulin at a given age and early death. This is not strictly because insulin makes you age, though. It is because the pancreas makes extra insulin as a way to compensate for a steady decrease in insulin's effectiveness in getting the rest of the body, especially our muscle, to absorb excess sugar in the blood. That decrease is in turn caused by various factors including accumulation of excess fat inside muscle fibres. And that, of course, is caused by overeating and bad diet and so on. But at the sharp end, what makes you age faster in all this is the excess sugar that insulin tries to get muscle to absorb, not the insulin itself. (Excess sugar does bad things to proteins, especially in the form of stiffening the arteries and other tissues, causing high blood pressure and its sequelae such as kidney damage.)

This is an example of a pretty general rule in aging: if a change with age is under genetic control (as insulin level is, because insulin is a protein), it's almost always an adaptation that minimises the rate of aging in response to other things, rather than a contributor to aging in its own right.

##### What is the best way to learn about 'anti-aging' technologies?
Read sens.org and fightaging.org

##### How close are we to decoding the aging process and living for either a very long period of time, or indefinitely?
My prediction is that we have a 50% chance of reaching "longevity escape velocity" within 20-25 years. That means getting good enough at preventing age-related ill-health that we will be postponing it faster than time is passing, keeping one step ahead of the problem by the development of progressively more effective and comprehensive therapies. This is, however, very much subject to the availability of enough funding to let today's early-stage research proceed as fast as the science allows. In the past nine years since I've been making timeframe predictions, we've probably brought the defeat of aging only about three years closer - and that's not because I was overoptimistic on the science, it's about how fast I would have said we would go given the funding that has in fact been available.

##### Are the efforts to create anti-aging technologies/remedies unethical?
The only reason why this question is not immediately seen to be absurd is because it relies on the audience not noticing the lack of any definition of what "anti-aging research" actually is. When you think for a second (only a second, really) about what "anti-aging research" might be, you can see that it in turn depends on a proper definition of what "aging" is, which is a colossal source of self-deceit in society. The fact is, aging is the lifelong process (or set of processes, if you prefer) that eventually gives rise to the diseases and disabilities of old age. Therefore, anti-aging research is medical research - medical research to develop preventative medicine for the diseases and disabilities of old age. There is no ambiguity or controversy about this: that's what anti-aging research is, no more and no less. So, if you seek to question whether anti-aging research is ethical, you must start by accepting that you are also questioning whether preventative medicine for the diseases and disabilities of old age is ethical. And I don't often find people willing to accept that. There tends to be a rather deafening silence when people who are against anti-aging research are challenged to assert that they think the diseases and disabilities of old age should not be prevented.

##### How does Fullerene manage to increase lifespan in both rats and mice?
This is still a controversial topic. The Algerian study published recently has a number of flaws that have led many people to doubt its reproducibility; however, it must also be borne in mind that Dugan's group found impressive benefits in a study published back in 2008 (PubMed 17079053, following up on 15451059 - I guess you know about this one because you mention mice as well as rats, but it has been largely forgotten). I still like the theory that it works by being a very unreactive radical due to extreme delocalisation of unpaired electrons - but this too is unproven.

##### There are evidences that the less children people have the longer they live. It is easy to explain in the case of women who put a lot of energy into the pregnancy and breast-feeding. What about man?
It doesn't need to be that the process of having children shortens one's life: it could be that there exist factors that limit one's reproductive capacity and also, independently, slow one's aging. That's the model the authors favour, and it is plausible in both sexes, especially in terms of delay in the age of puberty.

##### Historically, what was your life expectancy given that you survived childhood?
Life Expectancy by Age, 1850-2004

Before anyone asks: no, I don't know why the life expectancy at ages above 40 actually went down from the 1850 baseline and didn't start rising again until 1920. My guess it it's a data reliability artifact rather than a real phenomenon.

##### Gerontology: How do I become a biomedical gerontologist from here?
Well, there's obviously no one answer - it depends heavily on your personal circumstances, not just your academic background. In 1995 or so when I decided to switch fields from computer science, I was fortunate enough that I was already doing my research in my spare time, which I had been able to arrange to have quite a lot of because my day job in bioinformatics was very undemanding. Thus, I was able to switch painlessly to spending my time in the library (yes, we used physical libraries back then :-)) and going to conferences to get to know the latest information and the leading scientists. It worked - I was able to come up with well-received ideas that were published in good journals. But after that I needed more luck, because there was nowhere to work on biomedical gerontology (hardly any gerontologists back then were even willing to talk about the prospects for intervention in aging). Luckily I came up with some ideas for intervention that were very new and exciting to some people, leading to the creation of a foundation, quite a bit of media attention, and then sizeable donations which have allowed me to fund research. These days it's a bit easier, because intervention is fashionable in the field now - so all you need is the first part, learning biology and impressing people who might employ you. All I would add about doing it in your spare time is that biology is a very "horizontal" field as compared to physics, maths etc - you can get away with learning things in a pretty much random order, just so long as you have a good memory, because facts/insights don't build on each other so much.

##### How close are we to finding a cure for aging?
"Cure" isn't the right word, because aging is the accumulation of molecular and cellular side-effects of the body-s normal operation; as such, there can never be a one-off treatment like a vaccine that makes us non-aging. What we will develop instead is treatments that repair those side-effects, and which we will use periodically so that the side-effects never build up to a level that causes ill-health. I think we have a 50% chance of getting there within 25 years. (That's extremely speculative, of course, like any long-term technological prediction, but so what? - the harder we try, the sooner we'll get there.)

The only real impediment at this point is the prevalence of attitudes such as those expressed by others here, along the lines of "we've never done it so we never will" or "aging is not a disease" etc. That sort of nonsense is an extremely seductive way to put aging out of our minds until it's too late, at which point we have no choice but to grin and bear it until we succumb, but personally I prefer to face up to the problem of aging and fix it, for me and for everyone else.

##### Is Life Extension Foundation Inc (LEF) scientifically reputable? What peer reviewed research have they supported?
I've very recently joined LEF's scientific advisory board, and as such this is the sort of thing I should know, but I didn't, so I asked, hence the slowness of my reply. For brevity I will just list some PubMed IDs:

23263938
12163699
22485140
19929256
17611063
16567370
16189280
15044709
15039484

I'm told that this is not a complete list. In particular, it does not include any of the work on tissue cryopreservation done at 21st Century Medicine, whose funding comes almost entirely from LEF; to a good approximation that means everything published by GM Fahy in the past decade, which is another 20 PubMed hits.

##### By approximately how many calories per day does metabolism slow with age?
This varies enormously from person to person - genetic, lifestyle and other influences all matter. For practical purposes, i.e. if your goal is to avoid gaining weight, the correct approach is not to look at indirect factors such as your caloric intake but rather to look directly at what is happening to your weight and adjust your caloric intake accordingly. Of course this does not exclude other key things like maintaining a balanced diet so that your micronutrient intake is also optimised.

##### Is it theoretically possible to stop or slow down aging?
Slowing it down, even a little bit, is very difficult, and stopping it is definitely impossible. But paradoxically, reversing it is relatively easy. SENS Research Foundation is spearheading the development of medicines to do that. See SRF Home | SENS Research Foundation for details.

##### Longevity: In order of durability, which parts of your body would be the first to give out, and which would be the last?
There's very little difference. If there were, that difference would diminish over generations, because if one body part were being maintained "unnecessarily well" so that it was still fine when the organism was dead through failure of other parts, the genes that encode that good maintenance would not have any selective pressure to avoid accumulating mild mutations that slightly impaired the maintenance until the relevant body part was roughly equal in longevity to the rest of the body.

##### How does sirolimus/rapamycin slow the aging process?
That is still very much an area of research, i.e. we don't know for sure. At this point, though, most experts believe that the mode of action is broadly that rapamycin is acting as a calorie restriction mimetic, or more specifically a protein restriction mimetic, via mildly inhibiting the activity of the ribosome, i.e. the synthesis of proteins.

##### What would the average life span be if science found a cure for aging?
The number you seek has been calculated by many researchers over the years and of course it is highly dependent on what dataset one starts with, since different populations have different rates of death from age-independent causes, but it generally comes out somewhere between 700 and 2000. However, it is quite clearly absurd to presume that risks of death from age-independent causes would remain at today's levels: they are declining anyway, and it is pretty much a given that they will decline faster once they become the only cause of death and we therefore care more. In practice I think it is extremely likely that at least 90% of those who make it to 200 as a result of medicine to overcome aging will live as near to forever as makes no difference.

##### What do we know about organisms that outlive humans? What key points can help to battle human aging?
We know quite a lot about such animals, but very little of what we know seems to be useful. Either the animal has no long-lived non-dividing cells (such as clams), or it is cold-blooded and typically grows throughout life (such as various fish, amphibians and reptiles), or it lives in a very warm constant-temperature environment (such as naked mole rats), or it's reeeeally big so its specific metabolic rate is lower (such as whales), or it doesn't actually live longer than us, only longer for its size (such as various birds). All these differences result in either the "aging problem" being not so severe for those species as for humans, such that the animal can live longer than us without having more sophisticated anti-aging tricks, or else the problem being ostensibly more severe but not in ways that necessarily matter for longevity. On top of that, a modestly more sophisticated anti-aging setup would almost certainly not point the way to a human therapy, because the benefits conferred by copying some genetic difference or other would be outweighed by the problems caused by trying to dovetail it with the highly optimised network of everything else that humans have.

The most promising exception to the above is the uncanny rarity of cancer in a variety of long-lived lower vertebrates, and also in naked mole rats. The incidence of cancer in such species appears to be so dramatically lower than in mammals (even humans) that there does seem to be a real chance of finding a trick that could be applied to humans without being outweighed by the dovetailing problem. Some of the best work on this is being done by the Gorbunova lab in Rochester.

Don't get too excited about the frozen frogs - they only go a little below 0oC. They do it by replacing a lot of their water with sugar. Certain lower species can do this better and go down to as low as -30 as I recall, but for useful cryopreservation in anticipation of revival when better medicine exists we need much lower temperatures than that: plenty of chemistry, in particular decay of tissue, still happens at -30.

##### Would it make sense for Aubrey De Grey and Ray Kurzweil to work together towards similar goals? Why/Why not?
Well, it depends what you mean by "work together". We know each other well and we regularly point journalists etc to each other when appropriate; obviously our views as to what medical research is needed to defeat aging (what Ray calls "bridge 2" are very similar and we appreciate each other's support. Whether it would make sense for us to work more closely together is less clear, because the people SENS Research Foundation works with tend to be bench scientists.

##### What technologies could have the most impact on extending human life?
Eliminating any single disease will give at most a few years - the only option for significant extension is postponing aging itself, i.e. the accumulation of molecular and cellular damage. The most feasible way to do that is to periodically repair the damage, which is what SENS Research Foundation are working to do. Improved communication is always good, but ultimately the one thing that's needed far more than anything else is more funding (for the entire effort, not only for SENS Research Foundation). I estimate that the relevant research is going only about 1/3 as fast as it could with ten times more money. (Our current budget is about $4M/year.)

##### What's a good template for a chart on risk management for longevity purposes?
Various organisations publish statistics on therelative incidence of death from different causes, stratified by age, region/nation, etc. However, such statistics are of really very minor importance in telling you how to act to minimise your own risks, because individual variation in circumstance and in genetics/metabolism are so huge. What matters most is to examine the details of how you live and how healthy you are, and do what works for you.

##### How a person can help in the development of anti-aging tools?
Well, the main thing I would say is that there isn't really anything more than "idea spread". The single thing that's missing from this crusade right now is funding, and ultimately that comes from the public one way or another - even independent philanthropists generally decide what to support on the basis of how they think their donation will be perceived by others. That's why I spend so much of my time on advocacy. It's every bit as important as working at the lab bench.

##### What does Aubrey de Grey think about non-biological proposals for life extension such as whole brain emulation/mind uploading?
It's honestly not my area of expertise - and that's not an accident. I'm a first-things-first, practical sort of guy. I focus on wetware because I see a reasonably detailed path to what I'm trying to achieve. I don't see such a path for any of the various non-biological proposals. But that said, let me also stress that I'm very pleased that others are pursuing those avenues, because as time passes they may overtake the straight biomedical approach in terms of plausibility.

##### What would be some interesting side effects of a sharp and pronounced increase in life extension?
The necessary precursor to answering your question is to clarify what "life expectancy" is. The headline numbers we hear each year about life expectancy are actually a really weird artificial construct that basically says how long someone born today would live if all risks of death at any age stayed the same forever into the future. Obviously that's insanely overpessimistic. So the question one must actually ask is how long people will live if progress occurs at a specified rate. But also, it depends what sort of progress. If we extend lifespan by methods that only work when applied to newborns, we'll have a very different situation than if the therapies work on those who are already in middle age (which I believe is much more likely).

##### What will be some interesting side-effects of living forever, both individually and as a society?
It is a perpetual source of sadness to me to see the way people answer this sort of question. I have no idea how otherwise rational, well-educated people can have such spectacularly blinkered imagination on this one topic.

The two main things, both excruciatingly obvious once you think of them, that seem to escape almost everyone are:

1) It takes a really long time to get to the point of having lived a really long time, and a really large amount of stuff happens during that time. People today have the opportunity of a vast array of experiences that were unavailable to anyone even a few decades ago. As such, boredom is a vanishingly unlikely prospect, especially given that it is overwhelmingly a product of inadequate education, which is one thing that will disappear as affluence grows and technology advances. Similarly, any social challenges that may seem likely to result from demographic changes in a post-aging world (such as having more people or fewer kids) must be evaluated in the context of what else may change before those changes become significant, such as the advent of alternative energy sources that reduce our carbon footprint.

2) What will happen soon - probably before the medical defeat of aging even arrives - is a huge change in how long people will EXPECT to live, on account of the impending arrival of those therapies. I predict that this change in what people expect will be very abrupt, resulting from progress in the lab reaching a perceived tipping-point of credible promise, and that it is probably less than a decade away. The thing is: at the same time, people will also have other expectations arising from the same source, specifically the expectation of not getting Alzheimer's and cancer and so on when they reach their eighties or thenabouts. And of not having to look after their parents when THEY get that way. And of not having to save for their retirement. And on and on. Accordingly, we have a moral obligation today to do our utmost (a) to hasten the development of such medicine, so as to alleviate as much suffering as we can, and (b) to forward-plan as best we can for this change in people's expectations and desires, since it will be very sudden and will cause a lot of turbulence that can be sharply ameliorated by said forward-planning.

##### What should everyone know about the biology of aging?
- aging is a natural side-effect of the normal operation of the human body

- being "natural" doesn't make it good; diseases are natural too

- aging is not a unitary process, but a chaotic consequence of various imperfections of the body's automatic self-maintenance processes

- aging has no evolutionary value; it exists because it doesn't do enough evolutionary harm to drive the improvement in those self-maintenance processes

- all age-related diseases are consequences of aging, so medical control of aging is just preventative geriatrics, not science fiction (though we can't significantly control aging yet)

- there is still plenty we don't know about the processes that drive aging, but we do know quite thoroughly what changes accumulate in the body that eventually drive the emergence and progression of age-related disease, and that may be pretty much all we need to know in order to develop treatments

- public ignorance about most of the above points is spectacularly prevalent, despite the best efforts of high-profile gerontologists to educate people. This is powerfully slowing down the development of treatments and costing a vast number of lives. Resistance to being educated about aging is a heritage of the time when truly effective anti-aging medicine was inconceivable and we needed to put it out of our minds. The more we can do to change that, the more lives will be saved and suffering alleviated.

##### What should everyone know about longevity, life extension, and extending one's lifespan?
- Nothing available today helps significantly, unless you count the really obvious things like not smoking or getting overweight

- It's virtually certain that no simple "magic bullet" therapy will ever do so

- Regenerative medicine, on the other hand, provides a route to a divide-and-conquer, multi-component therapy that has genuine potential to bring aging under true medical control

- It's still at least 20 years off

- The better the current work in this direction is funded, the sooner it'll succeed

- Above all, that means getting people to understand that aging is the origin of all age-related diseases, disabilities and death, and thus that treating aging is just preventative medicine for those conditions, not some kind of inappropriate interference with nature

##### What do we know about aging in non-mammals?
We know quite a lot. In brief outline:

- Plants, jellyfish, anemones, hydra and a few other examples come under the category of species that have no long-term non-dividing cells. In a very real sense, the possession of such cells is what most clearly distinguishes a multicellular organism from a clum (or film) of single-celled organisms: more clearly than the usual definition, which is the possession of a germline/soma distinction. That's because cell division is a massively powerful rejuvenating process, diluting and selecting away damage caused by the cell's normal operation. So such species tend to age very slowly if at all, but that tells us very close to nothing about how to combat aging in humans.

- Insects age pretty much like us. The only big difference is that a lot of insects (and other small invertebrates) have the capacity to enter a state of suspended animation variously known as diapause, dauer, anhydrobiosis etc, where they age many times more slowly than normal. Again it is unclear that this really tells us anything useful about combating human aging, even though the upstream parts of the genetic pathways involved are in many cases quite conserved in humans, basically because the downstream parts are not.

- Larger invertebrates like lobsters, and also various lower vertebrates, are potentially more interesting because they have non-dividing cells like neurons and so on, like us, and yet they live a very long time. However, they have "indeterminate growth" - they continue to grow throughout adulthood. This imposes a requirement to add cells to all tissues (even the brain), which means they can also compensate for death of cells in any tissue (so long as it is slow enough). So again it's a short cut that we don't have, because we have a fixed adult body size which has led evolution to favour the short-termist option of keeping such cells alive for as long as possible while not retaining the ability to replace ones that die. However, in this case there is a much better chance that we could learn something therapeutic from such species, by figuring out how to (re)activate such cell replacement.

- Then there's birds (and also bats, which of course ARE mammals, but that's a good thing, in that they're closer to us genetically). These species (well, not all birds) age very slowly for their body size, and they don't have any of the above short cuts to longevity. However, taking all factors into account (monst importantly body size, which determines how much oxygen each cell has to consume and free radicals it thereby risks making), even the best such species are only a little bit better than us, and what they do have over us is almost certainly the sum of a large number of subtle genetic changes, so exploiting any knowledge we might get of that (however detailed) would entail an impractical amount of dovetailing of their metabolism with ours. In practice we would quite definitely do more harm than good by introducing such tricks.

##### How important is Angiotensin I-Converting Enzyme in the aging process?
There was a recent report of an association of an ACE deletion with longevity. However, the key thing to remember in all such cases is that the difference in longevity associated with such alleles is really small. Even the classic example of ApoE4 gives only a modest longevity risk. For practical purposes, the priority in medical research needs to be the development of therapies that work for everyone, regardless of their genotype.

##### What are some notable advances in life extension?
If by "implementable" you mean advances that people can apply today to extend their lives, there aren't any (for most people). It's as good an idea as it ever was to avoid shortening your life by smoking, getting overweight etc, but beyond that one reaches diminishing returns unless one is unlucky in some specific way that can be somewhat normalised using supplements etc. For serious postponement of age-related ill-health, we need therapies that don't yet exist. That's why SENS Fondation exists.

##### Which startup is doing the most to extend human longevity?
There are quite a few. A good guide to the best ones right now is those funded by Thiel Foundation's Breakout Labs; I'm very pleased to say that a number of new companies with strong connections to SENS Foundation and with really exciting technology are among their early beneficiaries.

##### How can we transform the way we think about aging and begin to think about it as yet another disease - or the cause of multiple age-related diseases?
The first and most essential step is to get prominent biologists to tell it like it is about aging, on camera. The reason they don't comes down to many issues, including simple ignirance of the facts, self-interest in perpetuating their own funding, and above all the fact that quite a few vocal biologists are just as resistant to thinking of aging as a target for medical intervention as most non-biologists are.

##### There is a good possibility that aging - the old foe of being - will get defeated in the future, and that future can be much nearer if more time and resources are devoted to this quest, what is the most pragmatic way to engage more resources into this quest?
The main thing we need to do to get more resources assigned to the project is to change the public's attitude to the feasibility and desirability of bringing aging under medical control. Despite all the effort by gerontologists (not least myself) to create a better understanding of the fact that treating aging is synonymous with preventative geriatrics, there remains enormous public resistance to accepting it. This is largely because there are still lots of respected people, including biologists, out there reinforcing this misconception. Check Youtube for my debate with Colin Blakemore in April, which illustrates the problem in spades.

##### What are some mind-blowing facts about the biology of aging?
Apparently, though much to my enduring disgust, most people find it mind-blowing that aging is simply the lifelong process that leads to age-related disease and disability, and that treatment of aging is thus synonymous with preventative geriatrics. If people understood this message - which has been expressed for decades - we would accelerate the development of such interventions by at least a factor of three in my view.

##### Is the concept of "Longevity Escape Velocity" (Aubrey de Grey) feasible?
Yes - but I would say that, wouldn't I? :-)

The key consideration here is that we don't know what biomedical technologies will be developed in the distant future, anything like so well as we know what's coming in the near future. The main reason why some scientists heap scorn on the LEV concept is because they intuitively presume that if we don't know what's going to happen we should presume that nothing much will happen, or at least that's how we should talk publicly. I see no justification whatsoever for that attitude. If we accept (as lots of the scientists I refer to above do) that there is a respectable chance of achieving what I call "robust human rejuvenation" (the addition of 30 years of healthy life to those already in middle age when treatment is initiated, via a suite of molecular and cellular regenerative medicine therapies) within the next 20-25 years, then it is logically impossible to deny that that buys us a lot of time to develop refinements of those therapies which allow the same people to be re-rejuvenated, etc, i.e. to maintain LEV. Whether it buys us ENOUGH time is certainly unknown, and my assertion that it almost certainly does is based on a belief that pretty much all the refinements that will be needed will be minor tweaks/extensions of the first-generation therapies that deliver RHR, as opposed to fundamental new therapies - a belief that others are certainly entitled to dispute. But what cannot be justified is the inverse belief: that therapies to re-rejuvenate people will almost certainly be so hard to develop that we will not achieve them in time to help the beneficiaries of RHR. That belief is founded on nothing more than an emotion-driven (or politically-driven, or similar) refusal to engage in rational inference on the matter.

##### Is Aubrey de Grey correct in the assertion that the average person can do more for their longevity by supporting anti-aging research than by spending time and money on fancy strategies to improve their health?
I'm not entirely sure why I've been asked to answer this question, since my own view is obviously already known. The essence of this logic is just that a great deal happens in a currently normal lifetime, and exactly what happens and how soon is under our control.

##### What are some examples of findings that have emerged from the SENS paradigm that would *not* have happened without the paradigm (either because people wouldn't have bothered to look, or wouldn't have been able to find it)?
SENS Foundation has published a number of papers on our efforts to identify non-human enzymes to break down intracellular garbage that causes age-related issues: most of them are from our Rice University group (search PubMed for author Mathieu JM). We also have work about to be submitted by our group at Albert Einstein College of Medicine on epimutations. However, what probably matters more in the long run is that other groups have been picking up on our work. The best example is that Janet Sparrow's group at Columbia have published work on the elimination of the causative factor in macular degeneration using methods we pioneered.

More generally, the key issue is whether the SENS paradigm is shifting the emphasis of research to take better account of the potential synergy between biogerontology and regenerative medicine. The best measure of that, at this stage, is the range of work that's going on in prestigious research institutes - I'mnot sure why you tied to exclude such work in the phrasing of your question. See SENS Foundation's 2011 research report for a wealth of good news in that regard:

http://www.sens.org/files/pdf/20...

##### If I am in my early twenties, should I bother with caloric restriction or should I sort of rely on medicine to advance enough by the time I would be old enough for it to make a difference?
There is a wide spectrum of opinion within the academic biogerontology community concerning the likely benefit of CR in humans. I personally am rather pessimistic, for reasons that I set out several years ago here:

http://www.ncbi.nlm.nih.gov/pubm...

But to answer your question directly: interventions that bring aging under genuine medical control, actually rejuvenating people rather than just slowing aging down, are still too far off for us to have any idea of exactly how far. So, no matter how young or old you are today, anything you can do to stay alive and healthy for as long as possible increases your chances of being around when those therapies do arrive. If you find it not too stressful to do CR, and you do it knowledgeably (according to the recommendations of the CR Society, for example), it probably won't hasten your aging - and if I'm wrong in my pessimism above, it might be worth doing.

##### Has anyone tracked the cause of death in fruit fly aging studies?
As far as I know it's never been done thoroughly. Desiccation and cuticle damage have been mentioned, but it would definitely be useful to study this more.

##### Longevity: What are the top 5 things we have learned about senescence in the 9 years since the start of the Methuslah Mouse Prize (http://www.mprize.org/)?
The great news is, we really haven't learned very much - in other words, what we have learned has mostly been rounding out details of what we knew before rather than overturning core tenets.

##### What are some of the top universities in the field of aging?
That depends what you mean by "the field of aging". If you mean biogerontology, the study of how aging happens and why, then there are a few stand-out places around the world, such as the University of Texas at San Antonio, though there are also a lot of places in which this topic is ony a minor area but where outstanding research is still done. But if you mean biomedical gerontology, the development of future medical interventions against aging, it is harder to identify the main places, because so much of the relevant research is done mainly for reasons other than intervening in aging. My own interests in that regard are mainly in the area of regenerative medicone, including stem cells and tissue engineering.

##### What daf-2 gene and foxo do for anti-aging?
The short answer is that those genes are among a family that are responsible for orchestrating a highly complex set of shifts in metabolic priorities in response to nutrient deprivation. In most model organisms, in most experiments, the result is a postponement of age-related ill-health and a consequently longer life. However, there are both evolutionary arguments and preliminary/anecdotal data suggesting (to me anyway, though not to all in the field) that the effect will be much smaller in long-lived animals like humans. See my paper in Gerontology 51:73 for more detail.

##### As breathing causes oxidative stress, would breathing less per minute increase life span in humans?
It turns out that no, the relationship between oxygen consumption rate and the rate of creation of damage caused by oxidative stress is not linear, nor even monotonic. The way mitochondria work means that the most dangerous situation is to have more mitochondria than you need for your rate of oxygen consumption. The body "knows" this and regulates mitochondrial number, so the real level of oxidative stress and oxidative damage is determined by subtler factors.

##### How would the world be different if the average human life span were 200 years?
The average lifespan, defined in any precise way (for example, the average age at death of everyone dying in a given calendar year) will only very briefly be in the range 150-500. Getting to 150 will require technology to keep us healthy, and that technology will keep us healthy indefinitely, so longevity will skyrocket.

##### If I wanted to start a calorie restricted diet in order to prolong my life, where should I start?
Visit the Calorie Restriction Society website:

http://calorierestriction.org/

##### What are some examples of people who restrict their calorie intake to prolong their lives?
Roy Walford is the best known; he was a prominent biogerontologist who started doing CR after his experience at Biosphere 2 and evangelised a lot about it. A fair few other biogerontologists do it; probably the best-known living one is Mark Mattson.

##### Does a theory exist yet as to why Buckyballs extend the lifespan of mice when ingested with olive oil?
There are serious doubts about the credibility of this study. My own greatest concern is that the olive oil treatment gave such a huge result - unlike C60, olive oil is a substance that has been studied extensively in this regard in the past with no such effect. I'm not thinking too much about this result until (unless) it is reproduced.

##### What are the most definitive medical tests to take to determine the precise biological processes that are contributing to one individual's aging?
Actually I don't talk about such tests - it's not my area - I work on the development of future therapies that will be so universally applicable that testing who needs them the most will be of only secondary importance.

##### Does Aubrey de Grey keep such a long beard for any reason other than fashion?
I have it because my wife likes it...

##### What supplements does Aubrey de Grey take to stay young, if any?
I don't take anything. I have the good fortune to be doing very well for my age as measured by very thorough tests (I was given Kronos's now-discontinued comprehensive screen three times in the past decade), so for me the best policy is "if it ain't broke don't fix it". People who have drawn short straws in the aging stakes should therefore not be guided by my choice in this.

##### Does resveratrol keep our cells from aging?
I don't have much to add to the answers already given. The ony thing I would add is that the evidence from mouse experiments is much more encouraging in relation to "metabolically challenged" mice (in particular, those fed a high-fat diet) than normal mice. Clearly some humans are more metabolically challenged than others; it's not unreasonable to infer that resveratrol (and its more potent analogues being developed by Sirtris) may also benefit humans with obesity or diabetic problems. However, as has been said, this must definitely be viewed as tentative at this point.

##### How does calorie restriction extend lifespan?
Standard answer: It works because the changed metabolic priorities in a famine, mostly resulting from the lowered imperative to procreate (since one's offspring have a high probability of dying of starvation before having their own), cause a slowdown in the accumulation of molecular and cellular damage with age. A big part of this is probably damaged proteins and organelles (such as mitochondria), since autophagy is accelerated, presumably so as to make amino acids and other small molecules available for reuse. Many people think this is how rapamycin works to extend mouse longevity, for example. See Cell 146:682 for a good recent review.

##### Aubrey de Grey: Were you inspired by Heinlein's fictional Howard Foundation in his Future History stories?
No - I always knew that aging was a bad thing and could in principle be defeated by medicine.

##### Is it possible for a human being to live for 900+ years?
The point here, of course, is that medicine that doesn't yet exist (a) may or may not be possible to develop and (b) may or may not postpone age-related ill-health by a certain amount. We'll only know the answers when we try to develop the medicine in question, and when, having done so, we apply it to people. But for sure humans of today cannot live appreciably longer than what has been seen, i.e. the world record of 122 years. Aging is caused mostly by internal, non-negotiable processes such as breathing; our environment (protection from radiation, etc) doesn't relate to that.

##### What is the relationship between metabolism and aging?
First, a terminological point: "metabolism" refers to all the molecular and cellular processes that go on in the body, not only breathing. It's only the term "metabolic rate" that specifically refers to oxygen consumption.

So: Yes, there is a correlation between what's called "specific metabolic rate", SMR (which means rate of oxygen consumption per unit body mass) and rate of aging, i.e. an inverse relationship between SMR and maximum potential lifespan. This is no surprise, because breathing is undoubtedly bad for you: it creates free radicals, which damage DNA and other macromolecules, and the rate of accumulation of that damage is a major determinant of the rate of aging. But it's only a modestly tight correlation, because the evolutionary pressure to avoid aging varies from one species to another, and that variation is dependent on many factors. So birds tend to live far longer than rodents of the same size (and thus of similar SMR), because evolution has worked harder on them to bear down on the rate of free radical production per unit oxygen consumption, the resistance of their macromolecules to being damaged by free radicals, etc.
